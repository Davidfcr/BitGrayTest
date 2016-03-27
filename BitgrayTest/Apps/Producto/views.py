from django.shortcuts import render
from django.shortcuts import redirect
from django.shortcuts import get_object_or_404
from django.forms import ModelForm
from .models import productos


class producto_form(ModelForm):
	class Meta:
		model = productos
		fields = ['producto', 'precio', 'descripcion']

def producto_create(request):
	form = producto_form(request.POST or None)
	if form.is_valid():
		form.save()
		return redirect('/crudmenu/productos/')
	return render(request, 'crudform.html', {'form':form})

def producto_update(request, pk):
	row = get_object_or_404(productos, id=pk)
	form = producto_form(request.POST or None, instance=row)
	if form.is_valid():
		form.save()
		return redirect('/crudmenu/productos/')
	return render(request, 'crudform.html', {'form':form})

def producto_delete(request, pk):
	row = get_object_or_404(productos, id=pk)
	if request.method=='POST':
		row.delete()
		return redirect('/crudmenu/productos/')
	return render(request, 'crudconfirmdelete.html', {'object':row})

