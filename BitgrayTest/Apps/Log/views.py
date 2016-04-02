from django.shortcuts import render
from django.shortcuts import redirect
from django.shortcuts import get_object_or_404
from django.forms import ModelForm
from .models import log
from Principal.serializers import LogSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status


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


@api_view(['GET', 'POST'])
def log_collection(request):
	""" API to list or create clients """
	if request.method == 'GET':
		log_list = log.objects.all()
		serializer = LogSerializer(log_list, many=True)
		return Response(serializer.data)
	elif request.method == 'POST':
		serializer = LogSerializer(data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def log_element(request, pk):
	""" API to list a sinlge client """
	try:
		log_list = log.objects.get(id=pk)
	except log.DoesNotExist:
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

	if request.method == 'GET':
		serializer = LogSerializer(log_list)
		return Response(serializer.data)
