# Generated by Django 3.2.4 on 2021-06-16 23:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clientes', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='modelocliente',
            name='dni',
            field=models.IntegerField(help_text='Escribir numero sin puntos', max_length=15, unique=True),
        ),
    ]