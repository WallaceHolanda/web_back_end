# Generated by Django 4.0.5 on 2022-06-15 02:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('produtos', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='produtos',
            name='imagem',
        ),
    ]
