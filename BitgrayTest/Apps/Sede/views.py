from django.shortcuts import render
from django.shortcuts import redirect
from django.shortcuts import get_object_or_404
from django.forms import ModelForm
from .models import sedes
from Principal.serializers import SedeSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status


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


@api_view(['GET', 'POST'])
def sede_collection(request):
	""" API to list or create clients """
	if request.method == 'GET':
		sedes_list = sedes.objects.all()
		serializer = SedeSerializer(sedes_list, many=True)
		return Response(serializer.data)
	elif request.method == 'POST':
		serializer = SedeSerializer(data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def sede_element(request, pk):
	""" API to list a sinlge client """
	try:
		sedes_list = sedes.objects.get(id=pk)
	except sedes.DoesNotExist:
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

	if request.method == 'GET':
		serializer = SedeSerializer(sedes_list)
		return Response(serializer.data)