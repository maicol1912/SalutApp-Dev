# Generated by Django 4.0.6 on 2022-10-25 16:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('database', '0003_alter_usuario_usuario_altura_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuario',
            name='usuario_altura',
            field=models.IntegerField(),
        ),
    ]
