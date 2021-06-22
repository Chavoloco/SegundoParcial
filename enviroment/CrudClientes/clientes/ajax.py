from django.http import JsonResponse
from .models import Clientes


def eliminar_cliente(request):
    pk = request.POST.get("cliente_id")
    cliente = Clientes.objects.get(pk=pk)
    cliente.delete()
    response = {}
    return JsonResponse(response)
