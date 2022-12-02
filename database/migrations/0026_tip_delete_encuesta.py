# Generated by Django 4.0.6 on 2022-11-26 19:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('database', '0025_remove_encuesta_encuesta_estado_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tip',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tip_encabezado', models.CharField(max_length=200)),
                ('tip_desc', models.TextField()),
            ],
        ),
        migrations.DeleteModel(
            name='Encuesta',
        ),
    ]
