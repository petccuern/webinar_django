from django.contrib import admin
from .models import *

# Register your models here.

class LivroAdmin(admin.ModelAdmin):
    list_display=('titulo','sinopse','data_publicacao','id')


class QuemAlugouAdmin(admin.ModelAdmin):
    list_display=('cliente','titulo')

admin.site.register(Livro, LivroAdmin)
admin.site.register(Autor)
admin.site.register(QuemAlugou, QuemAlugouAdmin)