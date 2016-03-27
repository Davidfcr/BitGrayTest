from django.shortcuts import render
from django.shortcuts import redirect
from django.shortcuts import get_object_or_404
from django.forms import ModelForm
from django import forms
from .models import compras


class compra_form(ModelForm):
	class Meta:
		model = compras
		fields = ['id_cliente', 'id_producto', 'id_sede', 'precio', 'descripcion', 'fecha']

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

class compra_interfaz(forms.ModelForm):
	"""Formulario para la interfaz de compra punto 4"""
	id_cliente = forms.CharField(widget=forms.TextInput(), label='Cliente', 
		required=True)
	id_producto = forms.CharField(widget=forms.TextInput(), label='Producto', 
		required=True)
	id_sede = forms.CharField(widget=forms.TextInput(), label='Cliente', 
		required=True)
	precio = forms.CharField(widget=forms.TextInput(), label='Cliente', 
		required=True)
	descripcion = forms.CharField(widget=forms.TextInput(), label='Cliente', 
		required=True)
	fecha = forms.CharField(widget=forms.TextInput(), label='Cliente', 
		required=True)

	class Meta:
		model = compras
		fields = ['id_cliente', 'id_producto', 'id_sede', 'precio', 'descripcion', 'fecha']

def compras_interfaz(request):
	form = compra_form(request.POST or None)
	if form.is_valid():
		form.save()
		return redirect('/crudmenu/compras/')
	return render(request, 'crudform.html', {'form':form})