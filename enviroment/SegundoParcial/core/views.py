from django.shortcuts import render


def index(request):
    # contenido = {"nombre_sitio": "LibrosOnline"}
    # return HttpResponse("Hola Mundo!.")
    return render(request, "core/template/index.html")
