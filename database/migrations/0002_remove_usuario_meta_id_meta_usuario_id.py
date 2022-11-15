# Generated by Django 4.0.6 on 2022-10-25 15:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('database', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='usuario',
            name='meta_id',
        ),
        migrations.AddField(
            model_name='meta',
            name='usuario_id',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='database.usuario'),
            preserve_default=False,
        ),
    ]