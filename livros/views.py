from django.shortcuts import redirect, render
from .models import *
from .forms import *

# Create your views here.

app_name='livros'

def lista_livros(request):
    livro=Livro.objects.all()
    return render(request, 'livros/lista_livros.html', {'livro':livro})


def ver_livro(request, id):
    livro=Livro.objects.get(id=id)
    alugou=QuemAlugou.objects.filter(titulo=livro)
    return render(request, 'livros/ver_livro.html', {'livro':livro, 'alugou':alugou})


def cadastrar_livros(request):
    form= LivroForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('livros:lista_livros')
    else:
        return render(request, 'livros/cadastrar_livros.html', {'form':form})


def editar_livros(request, id):
    livro=Livro.objects.get(id=id)
    form=LivroForm(request.POST or None, instance=livro)

    if form.is_valid():
        form.save()
        return redirect('livros:lista_livros')
    else:
        return render(request, 'livros/editar_livros.html', {'form':form})


def alugar(request, id):
    livro=Livro.objects.get(id=id)
    alugou=QuemAlugou() # Criei um objeto do tipo 'QuemAlugou', é semelhante ao formato de cadastr, mas neste caso nao precisa de um formluário, pois dessa forma nós editamos ou criamos atraves da propria view.
    
    livro.estoque-=1
    alugou.titulo=livro
    alugou.cliente=request.user

    alugou.save()
    livro.save()
    return redirect('livros:lista_livros')


def devolver(request, id):
    livro=Livro.objects.get(id=id)
    alugou=QuemAlugou.objects.filter(cliente=request.user) #aqui estou filtrando todos os objetos da minha classe 'QuemAlugou' pelo nome do cliente.
    for i in alugou:
        if livro == i.titulo:
            livro.estoque+=1
            i.delete()
            livro.save()
            return redirect('livros:lista_livros')
        else:
            continue
    return redirect('livros:lista_livros')
