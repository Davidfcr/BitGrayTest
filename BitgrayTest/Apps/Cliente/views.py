from django.shortcuts import render
from django.shortcuts import redirect
from django.shortcuts import get_object_or_404
from django.forms import ModelForm
from .models import clientes


class cliente_form(ModelForm):
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
