from django.shortcuts import render
from clientes.models import Clientes
from django.views import generic


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
    paginate_by = 5

    # def get_queryset(self):
    #     return Clientes.objects.filter(nombre__icontains="jer")[
    #         :5
    #     ]  # Get 5 clientes containing the name jer
