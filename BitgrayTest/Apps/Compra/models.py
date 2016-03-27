from __future__ import unicode_literals
from django.db import models


class compras(models.Model):
	"""Modelo clase de compras de bdpruebapython"""
	id = models.AutoField(primary_key=True)
	id_cliente = models.ForeignKey('Cliente.clientes', null=True, blank=True, default = None, db_column="id_cliente")
	id_producto = models.ForeignKey('Producto.productos', null=True, blank=True, default = None, db_column="id_producto")	
	id_sede = models.ForeignKey('Sede.sedes', null=True, blank=True, default = None, db_column="id_sede")		
	precio = models.PositiveIntegerField(null=True, blank=True)
	descripcion = models.TextField()
	fecha = models.DateTimeField(null=True, blank=True)
	class Meta:
		db_table = 'compras'

	def __unicode__(self):
		return self.id