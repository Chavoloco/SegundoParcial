from django.conf.urls import url
from . import views


urlpatterns = [
    url(r"^$", views.index, name="index"),
    url(r"^clientes_list/$", views.listaClientes.as_view(), name="clientes_list"),
]
