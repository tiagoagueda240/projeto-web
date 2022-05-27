# python manage.py runserver
from django.urls import path
from django.shortcuts import render
from . import views

app_name = "portfolio"

urlpatterns = [
    path('', views.home_page_view, name='home'),
    path('home', views.home_page_view, name='home'),
    path('sobre-mim', views.sobre_mim_view, name='sobre-mim'),
    path('projetos', views.projetos_view, name='projetos'),
    path('web', views.web_view, name='web'),
    path('blog', views.blog_view, name='blog'),
    path('criar/', views.nova_tarefa_view, name='criar'),
    path('editar/<int:tarefa_id>', views.edita_tarefa_view, name='editar'),
    path('apagar/<int:tarefa_id>', views.apaga_tarefa_view, name='apagar'),
    path('contactos', views.contactos_view, name='contactos'),
    path('login', views.login_view, name='login'),
    path('quizz', views.quizz, name='quizz'),
]
