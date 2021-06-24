from django.db import models
from django.db.models.deletion import CASCADE

# Create your models here.

class Autor(models.Model):
    autor= models.CharField(max_length=50)
    
    def __str__(self):
        return self.autor


class Livro(models.Model):
    titulo= models.CharField(max_length=50)
    sinopse= models.TextField()
    estoque= models.IntegerField(default=1)
    data_publicacao= models.DateField()
    autor= models.ManyToManyField('Autor')

    quem_alugou=models.ManyToManyField('users.User', blank=True, null=True)

    def __str__(self):
        return self.titulo


class QuemAlugou(models.Model):
    titulo = models.ForeignKey('Livro', on_delete=CASCADE)
    cliente = models.ForeignKey('users.User', on_delete=CASCADE)

    def __str__(self):
        return self.cliente
