from django.shortcuts import render, redirect

from .forms import *
from .models import *

# Create your views here.

def registro(request):
    form=RegisterForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('livros:lista_livros')
    else:
        return render(request,'users/registro.html', {'form':form})
















# def registro(request):
#     form=RegisterForm(request.POST or None)
#     if form.is_valid():
#         form.save()
#         return redirect('home')
#     else:
#         return render(request, 'users/registro.html',{'form':form})
