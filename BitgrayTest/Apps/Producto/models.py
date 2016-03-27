from __future__ import unicode_literals
from django.db import models


class productos(models.Model):
	"""Modelo clase de compras de bdpruebapython"""
	id = models.AutoField(primary_key=True)
	producto = models.CharField(max_length=40, null=True, blank=True)
	precio = models.PositiveIntegerField(null=True, blank=True)
	descripcion = models.TextField()
	class Meta:
		db_table = 'productos'

	def __unicode__(self):
		return self.producto

