# Generated by Django 4.0.6 on 2022-11-18 03:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('database', '0011_alter_usuario_usuario_peso'),
    ]

    operations = [
        migrations.AddField(
            model_name='especificacion',
            name='especificacion_recomendaciones',
            field=models.TextField(default=2),
            preserve_default=False,
        ),
    ]
