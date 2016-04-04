# coding=utf-8
# -*- coding: utf8 -*-
# vim: set fileencoding=utf8 :
""" A single context processor created to send a weekly report. I could use celery but this seems more simple """
from django.conf import settings
from django.core.mail import EmailMultiAlternatives
from Producto.models import productos
from Compra.models import compras
from django.db.models import Avg
from django.db.models import Max
from django.db.models import Sum
from django.db.models.functions import Coalesce
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from itertools import chain
import datetime
import smtplib

def weekly_report(request):
    """  Start the task counter """
    restart_enviar()
    if settings.TASK_ENVIAR:
    	if datetime.datetime.now().isocalendar()[2] == 7:
    		try:
    			emisor = settings.DEFAULT_FROM_EMAIL
    			para = [settings.DEFAULT_TO_EMAIL]
    			asunto = u'Reporte semanal'
    			mensaje = reporte_msg()
    			msg = EmailMultiAlternatives(asunto, mensaje, emisor, para)
    			msg.attach_alternative(mensaje, "text/html")
    			msg.send()
    			settings.TASK_ENVIAR = False
    		except smtplib.SMTPException:
    			raise
    return {}

def restart_enviar():
	if datetime.datetime.now().isocalendar()[2] == 2:
		settings.TASK_ENVIAR = True
	return

def reporte_msg():
	"""
	a. Diferencia promedio, máxima y mínima entre tabla productos columna
	precio y tabla compras columna precio.
	b. Número de compras.
	c. Total ganancias.
	d. Compras promedio por minuto.
	"""
	precioprodprom = int(productos.objects.aggregate(Avg('precio'))['precio__avg'])
	preciocromprom = int(compras.objects.aggregate(Avg('precio'))['precio__avg'])
	diferenciaprom = abs(precioprodprom - preciocromprom)

	productosprecio_list = productos.objects.values_list('precio', flat=True)
	comprasprecio_list = compras.objects.values_list('precio', flat=True)
	precio_list = list(chain(productosprecio_list, comprasprecio_list))
	maxprecio = max(precio_list)
	minprecio = min(precio_list, 0)

	totalcompras = int(compras.objects.aggregate(Sum('precio'))['precio__sum'])

	compras_list = compras.objects.all().count()
	compras_list_f = compras.objects.first()
	compras_list_l = compras.objects.latest('id')
	diff = compras_list_f.fecha - compras_list_l.fecha
	compraporminuto = abs(diff.total_seconds() / 60) / compras_list

	html_contenido = ('<b>Diferencia promedio</b>: 'u'{0} <br/> <b>máxima</b>: 'u'{1} <br/> <b>mínima</b>: 'u'{2} <br/>').format(diferenciaprom, maxprecio, minprecio)
	html_contenido += ('<b>Numero de compras</b>: 'u'{0} <br/>').format(compras_list)
	html_contenido += ('<b>Total ganancias</b>: 'u'{0} <br/>').format(totalcompras)
	html_contenido += ('<b>Compras promedio por minuto</b>: 1 compra cada 'u'{0} <br/>').format(compraporminuto)
	return html_contenido

