# Generated by Django 4.0.5 on 2022-06-15 11:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('produtos', '0003_produtos_imagem'),
    ]

    operations = [
        migrations.AlterField(
            model_name='produtos',
            name='imagem',
            field=models.CharField(max_length=255, null=True),
        ),
    ]
