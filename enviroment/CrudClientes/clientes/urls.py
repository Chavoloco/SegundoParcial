from django.conf.urls import url
from . import views


urlpatterns = [
    url(r"^$", views.index, name="index"),
    url(r"^clientes_list/$", views.listaClientes.as_view(), name="clientes_list"),
    url(r"^cliente/create/$", views.CrearCliente.as_view(), name="cliente_create"),
    url(
        r"^cliente/(?P<pk>\d+)/update/$",
        views.ActualizarCliente.as_view(),
        name="cliente_update",
    ),
    url(
        r"^cliente/(?P<pk>\d+)/delete/$",
        views.EliminarCliente.as_view(),
        name="cliente_delete",
    ),
]
