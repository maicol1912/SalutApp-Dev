# Generated by Django 4.0.6 on 2022-11-26 17:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('database', '0020_alter_tarea_tarea_check_1_alter_tarea_tarea_check_2_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='tarea',
            name='nro_tarea',
            field=models.IntegerField(null=True),
        ),
    ]
