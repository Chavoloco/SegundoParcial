from django.shortcuts import render
from clientes.models import Clientes
from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

# from .models import Clientes


def index(request):
    """
    Función vista para la página inicio del sitio.
    """
    # Genera contadores de algunos de los objetos principales
    num_clientes = Clientes.objects.all().count()

    # Numero de visitas a esta view, como está contado en la variable de sesión.
    num_visits = request.session.get("num_visits", 0)
    request.session["num_visits"] = num_visits + 1

    # Renderiza la plantilla HTML index.html con los datos en la variable contexto
    return render(
        request,
        "index.html",
        context={
            "num_clientes": num_clientes,
            "num_visits": num_visits,
        },
    )
    # Carga la plantilla index.html con la información adicional en la variable context.
    return render(request, "index.html", context=context)


class listaClientes(generic.ListView):
    model = Clientes
    paginate_by = 10

    def get_queryset(self):
        self.cliente = get_object_or_404(cliente, name=self.kwargs["Clientes"])
        return Clientes.objects.filter(cliente=self.cliente)

    # def get_queryset(self):
    #     return Clientes.objects.filter(nombre__icontains="jer")[
    #         :5
    #     ]  # Get 5 clientes containing the name jer


class CrearCliente(CreateView):
    model = Clientes
    fields = "__all__"
    success_url = "/clientes/clientes_list/"
    # initial = {
    #     "date_of_death": "05/01/2018",
    # }


class ActualizarCliente(UpdateView):
    model = Clientes
    # fields = ["nombre", "apellido", "pais", "telefono", "direccion", "dni"]
    fields = "__all__"
    success_url = "/clientes/clientes_list/"


class EliminarCliente(DeleteView):
    model = Clientes
    success_url = "/clientes/clientes_list/"
    # success_url = reverse_lazy("Clientes")
