# Generated by Django 5.0.6 on 2024-07-03 00:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0002_articulos_imagen'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='articulos',
            name='correo',
        ),
        migrations.RemoveField(
            model_name='articulos',
            name='facebook',
        ),
        migrations.RemoveField(
            model_name='articulos',
            name='instagram',
        ),
        migrations.RemoveField(
            model_name='articulos',
            name='nombre',
        ),
        migrations.RemoveField(
            model_name='articulos',
            name='numero',
        ),
        migrations.AlterField(
            model_name='articulos',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False, verbose_name='Clave'),
        ),
    ]