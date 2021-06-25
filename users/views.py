from django.shortcuts import render, redirect
from django.contrib.auth import logout

from .forms import *
from .models import *

# Create your views here.
app_name='users'

def registro(request):
    form=RegisterForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('livros:lista_livros')
    else:
        return render(request,'users/registro.html', {'form':form})


def logout_view(request):
    logout(request)
    return redirect ('/accounts/login')















# def registro(request):
#     form=RegisterForm(request.POST or None)
#     if form.is_valid():
#         form.save()
#         return redirect('home')
#     else:
#         return render(request, 'users/registro.html',{'form':form})
