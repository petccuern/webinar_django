from django.urls import path
from .views import *

urlpatterns = [
    path('lista_livros',lista_livros,name='lista_livros'),
    path('cadastrar_livros',cadastrar_livros,name='cadastrar_livros'),
    path('ver_livro/<int:id>',ver_livro, name='ver_livro'),
    path('editar_livros/<int:id>',editar_livros, name='editar_livros'),
    path('alugar/<int:id>',alugar, name='alugar'),
    path('devolver/<int:id>',devolver, name='devolver'),
]
