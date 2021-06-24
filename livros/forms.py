from django import forms
from .models import *

class LivroForm(forms.ModelForm):
    class Meta:
        model = Livro
        fields = ('titulo','sinopse','data_publicacao', 'autor')