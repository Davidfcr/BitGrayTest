from Cliente.models import clientes
from Producto.models import productos
from Sede.models import sedes
from Compra.models import compras
from Log.models import log
from rest_framework import serializers


class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = clientes
        fields = ('id', 'documento', 'nombres', 'detalles')


class ProductoSerializer(serializers.ModelSerializer):
    class Meta:
        model = productos
        fields = ('id', 'producto', 'precio', 'descripcion')


class SedeSerializer(serializers.ModelSerializer):
    class Meta:
        model = sedes
        fields = ('id', 'sede', 'direccion')


class CompraSerializer(serializers.ModelSerializer):
    class Meta:
        model = compras
        fields = ('id', 'id_cliente', 'id_producto', 'id_sede', 'precio', 'descripcion', 'fecha')


class LogSerializer(serializers.ModelSerializer):
    class Meta:
        model = log
        fields = ('id', 'fecha', 'descripcion')
