# Generated by Django 4.0.6 on 2022-10-26 02:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('database', '0004_alter_usuario_usuario_altura'),
    ]

    operations = [
        migrations.AddField(
            model_name='especificacion',
            name='especificacion_nombre',
            field=models.CharField(default=1, max_length=200),
            preserve_default=False,
        ),
    ]