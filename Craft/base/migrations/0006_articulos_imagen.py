# Generated by Django 5.0.6 on 2024-07-04 00:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0005_alter_articulos_producto'),
    ]

    operations = [
        migrations.AddField(
            model_name='articulos',
            name='imagen',
            field=models.ImageField(null=True, upload_to='fotos', verbose_name='Fotografía'),
        ),
    ]
