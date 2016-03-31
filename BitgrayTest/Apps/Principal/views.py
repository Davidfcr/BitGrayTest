from django.shortcuts import render
from Cliente.models import clientes
from Producto.models import productos
from Sede.models import sedes
from Compra.models import compras
from Log.models import log


def crudmenu_view(request):	
	"""List of the current BitgrayTest DB tables for CRUD """
	return render(request, 'crudmenu.html', 
		{'cliente': 'clientes', 'producto': 'productos', 'sede': 'sedes', 'compra': 'compras', 'log': 'log'})


def crudselect_view(request, nombretabla=None):
	tabla = None
	if nombretabla is not None:
		try:
			if nombretabla == 'clientes':
				tabla = clientes.objects.all()
				template = 'crudcliente.html'
			elif nombretabla == 'productos':
				tabla = productos.objects.all()
				template = 'crudproducto.html'
			elif nombretabla == 'sedes':
				tabla = sedes.objects.all()
				template = 'crudsede.html'
			elif nombretabla == 'compras':
				tabla = compras.objects.all()
				template = 'crudcompra.html'			
			elif nombretabla == 'log':
				tabla = log.objects.all()
				template = 'crudlog.html'
		except clientes.DoesNotExist:
			raise
		except productos.DoesNotExist:
			raise
		except sedes.DoesNotExist:
			raise
		except compras.DoesNotExist:
			raise
		except log.DoesNotExist:
			raise
	return render(request, template, {'lista': tabla})
