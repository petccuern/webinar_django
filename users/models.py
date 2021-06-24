from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class User(AbstractUser):
    tipo =(
        (1,'Cliente'),
        (2,'Funcionario')
    )
    
    tipo_usuario= models.IntegerField(choices=tipo, blank=True, null=True)

# all_fieds = User._meta.fields
# for i in all_fieds:
#     print(i)