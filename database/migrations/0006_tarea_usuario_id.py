# Generated by Django 4.0.6 on 2022-10-26 03:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('database', '0005_especificacion_especificacion_nombre'),
    ]

    operations = [
        migrations.AddField(
            model_name='tarea',
            name='usuario_id',
            field=models.ForeignKey(default=2, on_delete=django.db.models.deletion.CASCADE, to='database.usuario'),
            preserve_default=False,
        ),
    ]
