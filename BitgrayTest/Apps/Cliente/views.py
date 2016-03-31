from django.shortcuts import render
from django.shortcuts import redirect
from django.shortcuts import get_object_or_404
from django.contrib import messages
from django.forms import ModelForm
from .models import clientes
from Compra.models import compras


class cliente_form(ModelForm):
	"""Form used for CRUD"""
	class Meta:
		model = clientes
		fields = ['documento', 'nombres', 'detalles']

def cliente_create(request):
	form = cliente_form(request.POST or None)
	if form.is_valid():
		form.save()
		return redirect('/crudmenu/clientes/')
	return render(request, 'crudform.html', {'form':form})

def cliente_update(request, pk):
	row = get_object_or_404(clientes, id=pk)
	form = cliente_form(request.POST or None, instance=row)
	if form.is_valid():
		form.save()
		return redirect('/crudmenu/clientes/')
	return render(request, 'crudform.html', {'form':form})

def cliente_delete(request, pk):
	row = get_object_or_404(clientes, id=pk)
	if request.method=='POST':
		row.delete()
		return redirect('/crudmenu/clientes/')
	return render(request, 'crudconfirmdelete.html', {'object':row})


class facturacliente_form(ModelForm):
	"""Form returning the buyed products of an client document"""
	def __init__(self, *args, **kwargs):
		super(facturacliente_form, self).__init__(*args, **kwargs)
		self.fields['documento'].widget.attrs = {
			'required' : True
		}

	class Meta:
		model = clientes
		fields = ['documento']

def facturacliente_view(request):
	"""Handling the information of the facturacliente_form to responde with the client products"""
	sumtotal = 0
	form = facturacliente_form(request.POST or None)
	if request.method == 'POST':
		if form.is_valid():
			try:
				cliente_list = clientes.objects.get(documento=form.cleaned_data['documento'])
				compras_list = compras.objects.get(id_cliente=cliente_list.id)
				return render(request, 'facturatable.html', {'compras_list': compras_list})
			except clientes.DoesNotExist:
				messages.error(request, 'Cliente no existe')
			except compras.DoesNotExist:
				messages.error(request, 'El cliente no tiene compras asociadas')
			except clientes.MultipleObjectsReturned:
				messages.error(request, 'Existen varios clientes con el mismo documento')
			except compras.MultipleObjectsReturned:
				compras_list = compras.objects.filter(id_cliente=cliente_list.id)
				for item in compras_list:
					if item.precio is None: 
						sumtotal += item.id_producto.precio
					elif item.precio == 0:
						sumtotal += item.id_producto.precio
					else:
						sumtotal += item.precio
				return render(request, 'facturatable.html', {'compras_list': compras_list, 'sumtotal': sumtotal})
			finally:
				form = facturacliente_form			
		else:
			form = facturacliente_form
	return render(request, 'crudform.html', {'form': form})
