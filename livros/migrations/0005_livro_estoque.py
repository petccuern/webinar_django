# Generated by Django 3.2.4 on 2021-06-24 18:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('livros', '0004_auto_20210623_1507'),
    ]

    operations = [
        migrations.AddField(
            model_name='livro',
            name='estoque',
            field=models.IntegerField(default=1),
        ),
    ]
