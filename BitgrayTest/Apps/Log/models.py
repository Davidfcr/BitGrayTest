from __future__ import unicode_literals
from django.db import models


class log(models.Model):
	"""Modelo clase de compras de bdpruebapython"""
	id = models.AutoField(primary_key=True)
	fecha = models.DateTimeField(null=True, blank=True, )		
	descripcion = models.TextField()
	
	class Meta:
		db_table = 'log'

	def __unicode__(self):
		return self.fecha
