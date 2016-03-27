from __future__ import unicode_literals
from django.db import models


class sedes(models.Model):
	"""Modelo clase de compras de bdpruebapython"""
	id = models.AutoField(primary_key=True)
	sede = models.CharField(max_length=40, null=True, blank=True)	
	direccion = models.CharField(max_length=40, null=True, blank=True)
	class Meta:
		db_table = 'sedes'

	def __unicode__(self):
		return self.sede
