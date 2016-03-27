from django.shortcuts import render
from django.shortcuts import redirect
from django.shortcuts import get_object_or_404
from django.forms import ModelForm
from .models import sedes


class sede_form(ModelForm):
	class Meta:
		model = sedes
		fields = ['sede', 'direccion']

def sede_create(request):
	form = sede_form(request.POST or None)
	if form.is_valid():
		form.save()
		return redirect('/crudmenu/sedes/')
	return render(request, 'crudform.html', {'form':form})

def sede_update(request, pk):
	row = get_object_or_404(sedes, id=pk)
	form = sede_form(request.POST or None, instance=row)
	if form.is_valid():
		form.save()
		return redirect('/crudmenu/sedes/')
	return render(request, 'crudform.html', {'form':form})

def sede_delete(request, pk):
	row = get_object_or_404(sedes, id=pk)
	if request.method=='POST':
		row.delete()
		return redirect('/crudmenu/sedes/')
	return render(request, 'crudconfirmdelete.html', {'object':row})

