from django.shortcuts import render
from django.shortcuts import redirect
from django.shortcuts import get_object_or_404
from django.forms import ModelForm
from django.http import JsonResponse
from django.utils.translation import ugettext_lazy as _
from django import forms
from Cliente.models import clientes
from Producto.models import productos
from Sede.models import sedes
from .models import compras


class compra_form(ModelForm):
	class Meta:
		model = compras
		fields = ['id_cliente', 'id_producto', 'id_sede', 'precio', 'descripcion', 'fecha']
		widgets = {
			'fecha' : forms.SelectDateWidget(),
		}

def compra_create(request):
	form = compra_form(request.POST or None)
	if form.is_valid():
		form.save()
		return redirect('/crudmenu/compras/')
	return render(request, 'crudform.html', {'form':form})

def compra_update(request, pk):
	row = get_object_or_404(compras, id=pk)
	form = compra_form(request.POST or None, instance=row)
	if form.is_valid():
		form.save()
		return redirect('/crudmenu/compras/')
	return render(request, 'crudform.html', {'form':form})

def compra_delete(request, pk):
	row = get_object_or_404(compras, id=pk)
	if request.method=='POST':
		row.delete()
		return redirect('/crudmenu/compras/')
	return render(request, 'crudconfirmdelete.html', {'object':row})


class compra_interfaz_form(forms.Form):
	"""Formulario para la interfaz de compra punto 4"""
	OPT_PRODUCTOS = [('{0}-{1}'.format(opt.id, opt.precio), opt.producto) for opt in productos.objects.all()]	
	def __init__(self, *args, **kwargs):
		initial = kwargs.get('initial', {})
		initial['precio'] = productos.objects.first().precio
		kwargs['initial'] = initial

		super(compra_interfaz_form, self).__init__(*args, **kwargs)

		self.fields['cliente'].widget.attrs = {
			'required' : True
		}

		self.fields['producto'].widget.attrs = {
			'id' : 'productoint',
			'required' : True,
			'onchange' : 'obtenerValor()',
		}
		
	cliente = forms.ModelChoiceField(queryset=clientes.objects.all(), label='Cliente', )
	producto = forms.ChoiceField(choices=OPT_PRODUCTOS, label='Producto', )
	sede = forms.ModelChoiceField(queryset=sedes.objects.all(), label='Sede', )
	precio = forms.IntegerField(widget=forms.TextInput(), label='Precio', )
	descripcion = forms.CharField(widget=forms.Textarea(), label='Descripcion', )
	fecha = forms.DateField(widget=forms.SelectDateWidget(), label='Fecha',)

	class Meta:
		model = compras
		
class compra_interfaz(ModelForm):
	"""Formulario para la interfaz de compra punto 4"""
	def __init__(self, *args, **kwargs):
		initial = kwargs.get('initial', {})
		initial['precio'] = 0
		kwargs['initial'] = initial

		super(compra_interfaz, self).__init__(*args, **kwargs)
		self.fields['id_cliente'].widget.attrs = {
			'required' : True
		}

		self.fields['id_producto'].widget.attrs = {
			'id' : 'productoint',
			'required' : True,
		}

		self.fields['precio'].widget.attrs = {
			'required' : True,
		}

		self.fields['fecha'].widget = forms.SelectDateWidget()
		self.fields['fecha'].widget.attrs = {
			'required' : True
		}

	class Meta:
		model = compras
		fields = ('id_cliente', 'id_producto', 'id_sede', 'precio', 'descripcion', 'fecha')
		labels = {
            'id_cliente': _('Cliente'),
            'id_producto': _('Producto'),
            'id_sede': _('Sede'),
            'precio': _('Precio'),
            'descripcion': _('Descripcion'),
            'fecha': _('Fecha'),
        }
        
def compras_interfaz(request):
	"""Funcion para formulario de interfaz comrpas punto 4"""
	form = compra_interfaz(request.POST or None)
	if request.method == 'POST':
		if form.is_valid():
			form.save()
			return redirect('/crudmenu/compras/')
	return render(request, 'crudform.html', {'form':form})

def precioproducto(request, key):
	if request.method == 'GET':
		precio_producto = productos.objects.get(id=key).precio
		print precio_producto
		response_data ={}
		response_data['precio'] = precio_producto

	return JsonResponse(response_data)

