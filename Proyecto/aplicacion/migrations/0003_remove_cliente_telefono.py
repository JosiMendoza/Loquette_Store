# Generated by Django 5.0.6 on 2024-07-03 02:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('aplicacion', '0002_rename_usuario_cliente'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cliente',
            name='telefono',
        ),
    ]
