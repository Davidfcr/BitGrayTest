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
    url(r'^$', TemplateView.as_view(template_name='index.html')),
    # CRUD de tablas punto 1
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
    # Interfaz compras punto 4
    url(r'^compras/$', compras_interfaz, name='comprasinterfaz'),
    url(r'^precioproducto/(?P<key>\d+)/$', precioproducto, name='precioproducto'),
    # Consulta compras por cliente 5
    url(r'^facturacliente/$', facturacliente_view, name='facturacliente'),

]
