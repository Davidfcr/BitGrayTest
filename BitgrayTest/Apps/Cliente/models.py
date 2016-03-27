from __future__ import unicode_literals
from django.db import models


class clientes(models.Model):
	"""Modelo clase de clientes de bdpruebapython"""
	id = models.AutoField(primary_key=True)
	documento = models.IntegerField(null=True, blank=True)	
	nombres = models.CharField(max_length=80, null=True, blank=True)
	detalles = models.TextField()
	class Meta:
		db_table = 'clientes'

	def __unicode__(self):
		return self.nombres