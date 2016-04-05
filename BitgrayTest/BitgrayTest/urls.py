"""BitgrayTest URL Configuration"""
from django.conf.urls import url
from django.contrib import admin
from django.views.generic import TemplateView
from Principal.views import crudmenu_view
from Principal.views import crudselect_view
from Cliente.views import cliente_create
from Cliente.views import cliente_update
from Cliente.views import cliente_delete
from Cliente.views import facturacliente_view
from Cliente.views import facturapdf_view
from Producto.views import producto_create
from Producto.views import producto_update
from Producto.views import producto_delete
from Sede.views import sede_create
from Sede.views import sede_update
from Sede.views import sede_delete
from Compra.views import compra_create
from Compra.views import compra_update
from Compra.views import compra_delete
from Compra.views import compras_interfaz
from Compra.views import precioproducto
from Log.views import log_create
from Log.views import log_update
from Log.views import log_delete

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', TemplateView.as_view(template_name='index.html'), name='home'),
    # CRUD de tablas punto 2
    url(r'^crudmenu/$', crudmenu_view, name='crudmenu'),
    url(r'^crudmenu/(?P<nombretabla>[\w|\W]+)/$', crudselect_view, name='crudselect'),
    url(r'^crudclientecreate/$', cliente_create, name='crudclientecreate'),
    url(r'^crudclienteupdate/(?P<pk>\d+)/$', cliente_update, name='crudclienteupdate'),
    url(r'^crudclientedelete/(?P<pk>\d+)/$', cliente_delete, name='crudclientedelete'),
    url(r'^crudproductocreate/$', producto_create, name='crudproductocreate'),
    url(r'^crudproductoupdate/(?P<pk>\d+)/$', producto_update, name='crudproductoupdate'),
    url(r'^crudproductodelete/(?P<pk>\d+)/$', producto_delete, name='crudproductodelete'),
    url(r'^crudsedecreate/$', sede_create, name='crudsedecreate'),
    url(r'^crudsedeupdate/(?P<pk>\d+)/$', sede_update, name='crudsedeupdate'),
    url(r'^crudsededelete/(?P<pk>\d+)/$', sede_delete, name='crudsededelete'),
    url(r'^crudcompracreate/$', compra_create, name='crudcompracreate'),
    url(r'^crudcompraupdate/(?P<pk>\d+)/$', compra_update, name='crudcompraupdate'),
    url(r'^crudcompradelete/(?P<pk>\d+)/$', compra_delete, name='crudcompradelete'),
    url(r'^crudlogcreate/$', log_create, name='crudlogcreate'),
    url(r'^crudlogupdate/(?P<pk>\d+)/$', log_update, name='crudlogupdate'),
    url(r'^crudlogdelete/(?P<pk>\d+)/$', log_delete, name='crudlogdelete'),
    # API para consulta/creacion
    url(r'^apitest/$', TemplateView.as_view(template_name='APItestventana.html'), name='apitest'),
    url(r'^apicliente/$', 'Cliente.views.cliente_collection', name='cliente_collection'),
    url(r'^apicliente/(?P<pk>\d+)/$', 'Cliente.views.cliente_element', name='cliente_element'),
    url(r'^apiproducto/$', 'Producto.views.producto_collection', name='producto_collection'),
    url(r'^apiproducto/(?P<pk>\d+)/$', 'Producto.views.producto_element', name='producto_element'),
    url(r'^apisede/$', 'Sede.views.sede_collection', name='sede_collection'),
    url(r'^apisede/(?P<pk>\d+)/$', 'Sede.views.sede_element', name='sede_element'),
    url(r'^apicompra/$', 'Compra.views.compra_collection', name='compra_collection'),
    url(r'^apicompra/(?P<pk>\d+)/$', 'Compra.views.compra_element', name='compra_element'),
    url(r'^apilog/$', 'Log.views.log_collection', name='log_collection'),
    url(r'^apilog/(?P<pk>\d+)/$', 'Log.views.log_element', name='log_element'),
    # Interfaz compras punto 4
    url(r'^compras/$', compras_interfaz, name='comprasinterfaz'),
    url(r'^precioproducto/(?P<key>\d+)/$', precioproducto, name='precioproducto'),
    # Consulta compras por cliente 5
    url(r'^facturacliente/$', facturacliente_view, name='facturacliente'),
    url(r'^facturacliente/pdf$', facturapdf_view, name='facturapdf'),
]
