from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def tarefas_home(request):
    contexto = {
        "nome" : "lan"
    }
    return render(request, 'tarefas/home.html', contexto)     

def tarefas_adicionar(request):
    return HttpResponse("Adicione aqui suas tarefas.") 

def noticias(request):
    return render(request,'tarefas/noticias.html')
