# Generated by Django 4.0.6 on 2022-11-23 21:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('database', '0015_remove_tarea_id_remove_tarea_peso_check_4_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='tarea',
            name='peso_check_4',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]
