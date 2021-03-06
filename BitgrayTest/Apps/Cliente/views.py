from django.shortcuts import render
from django.shortcuts import redirect
from django.shortcuts import get_object_or_404
from django.views.decorators.csrf import csrf_exempt
from django.contrib import messages
from django.forms import ModelForm
from django.template import Context
from django.template.loader import get_template
from .models import clientes
from Compra.models import compras
from Principal.serializers import ClienteSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from django.http import HttpResponse
import cStringIO as StringIO
from xhtml2pdf import pisa
import json
from cgi import escape

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
						if item.id_producto is not None:
							if item.id_producto.precio is not None:
						 		sumtotal += item.id_producto.precio
					elif item.precio == 0:
						if item.id_producto is not None:
							if item.id_producto.precio is not None:
							 	sumtotal += item.id_producto.precio
					else:
						sumtotal += item.precio
				return render(request, 'facturatable.html', {'compras_list': compras_list, 'sumtotal': sumtotal})
			finally:
				form = facturacliente_form			
		else:
			form = facturacliente_form
	return render(request, 'crudform.html', {'form': form})

@csrf_exempt
def facturapdf_view(request):
	if request.method=='POST':
		try:
			data = json.loads(request.body.decode('utf-8'))
			render_to_pdf({'pagesize':'A4', 'lista': data})
		except Exception, e:
			str(e)

		return

def render_to_pdf(jsondata):
    try:
    	template = get_template('pdf.html')
    	context = Context(jsondata)
    	html = template.render(context)	
    	result = StringIO.StringIO()
    	pdf = pisa.pisaDocument(StringIO.StringIO(html.encode("ISO-8859-1")), result)
    	if not pdf.err:
    		return HttpResponse(result, content_type='application/pdf')
    	return HttpResponse('Errores<pre>%s</pre>' % escape(html))
    except Exception, e:
    	raise str(e)


@api_view(['GET', 'POST'])
def cliente_collection(request):
	""" API to list or create clients """
	if request.method == 'GET':
		clientes_list = clientes.objects.all()
		serializer = ClienteSerializer(clientes_list, many=True)
		return Response(serializer.data)
	elif request.method == 'POST':
		serializer = ClienteSerializer(data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def cliente_element(request, pk):
	""" API to list a sinlge client """
	try:
		if request.method == 'GET':
			clientes_list = clientes.objects.get(id=pk)
			serializer = ClienteSerializer(clientes_list)
			return Response(serializer.data)
	except clientes.DoesNotExist:
		return Response('No se encuentra cliente', status=status.HTTP_400_BAD_REQUEST)

	
