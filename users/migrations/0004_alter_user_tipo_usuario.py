# Generated by Django 3.2.4 on 2021-06-23 17:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_alter_user_tipo_usuario'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='tipo_usuario',
            field=models.IntegerField(choices=[(1, 'Cliente'), (2, 'Funcionario')]),
        ),
    ]
