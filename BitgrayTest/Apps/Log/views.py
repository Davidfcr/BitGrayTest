from django.shortcuts import render
from django.shortcuts import redirect
from django.shortcuts import get_object_or_404
from django.forms import ModelForm
from .models import log


class log_form(ModelForm):
	class Meta:
		model = log
		fields = ['fecha', 'descripcion']

def log_create(request):
	form = log_form(request.POST or None)
	if form.is_valid():
		form.save()
		return redirect('/crudmenu/log/')
	return render(request, 'crudform.html', {'form':form})

def log_update(request, pk):
	row = get_object_or_404(log, id=pk)
	form = log_form(request.POST or None, instance=row)
	if form.is_valid():
		form.save()
		return redirect('/crudmenu/log/')
	return render(request, 'crudform.html', {'form':form})

def log_delete(request, pk):
	row = get_object_or_404(log, id=pk)
	if request.method=='POST':
		row.delete()
		return redirect('/crudmenu/log/')
	return render(request, 'crudconfirmdelete.html', {'object':row})

