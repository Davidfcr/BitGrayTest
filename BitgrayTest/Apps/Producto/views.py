from django.shortcuts import render
from django.shortcuts import redirect
from django.shortcuts import get_object_or_404
from django.forms import ModelForm
from Principal.serializers import ProductoSerializer
from .models import productos
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status


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


@api_view(['GET', 'POST'])
def producto_collection(request):
	""" Class to list or create product via api """
	if request.method == 'GET':
		productos_list = productos.objects.all()
		serializer = ProductoSerializer(productos_list, many=True)
		return Response(serializer.data)
	elif request.method == 'POST':
		serializer = ProductoSerializer(data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def producto_element(request, pk):
    try:
        productos_list = productos.objects.get(id=pk)
    except productos.DoesNotExist:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    if request.method == 'GET':
        serializer = ProductoSerializer(productos_list)
        return Response(serializer.data)

