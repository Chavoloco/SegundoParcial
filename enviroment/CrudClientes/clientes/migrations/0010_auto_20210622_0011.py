# Generated by Django 3.2.4 on 2021-06-22 03:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clientes', '0009_alter_clientes_dni'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='clientes',
            options={'ordering': ['id']},
        ),
        migrations.AddField(
            model_name='clientes',
            name='foto',
            field=models.ImageField(default='##', upload_to='photos'),
        ),
    ]