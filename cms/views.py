from django.shortcuts import render
from django.http import HttpResponse

from .models import Pages
# Create your views here.
def inicio(request):
    lista = Pages.objects.all()
    respuesta = "<ul>"
    for elemento in lista:
        respuesta += "<li><a href=" +  str(elemento.id) + ">" + elemento.name + "</a>"
    respuesta += "</ul>"
    return HttpResponse("<h1>Welcome to this page, my friend, and check out our contents:</h1>" + respuesta)

def cms(request, numero):
    try:
        elemento = Pages.objects.get(id=str(numero))
    except Pages.DoesNotExist:
        return HttpResponse("<h1>This content {/" + str(numero) +  "} does not exist</h1>")
    return HttpResponse(elemento.name +": " + elemento.page)

