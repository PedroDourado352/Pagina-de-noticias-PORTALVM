from django.urls import path 
from . import views

app_name = "tarefas"

urlpatterns = [
    path("", views.tarefas_home),
    path("adicionar/", views.tarefas_adicionar, name="adicionar"),
    path('noticias/',views.noticias, name='noticias')
    ,path('noticia-detalhe/', views.noticia_detalhe, name='noticia_detalhe')
]
