from django.contrib import admin
from .models import *

# Register your models here.

class LivroAdmin(admin.ModelAdmin):
    list_display=('titulo','sinopse','data_publicacao','id')

admin.site.register(Livro, LivroAdmin)
admin.site.register(Autor)
admin.site.register(QuemAlugou)