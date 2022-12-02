# Generated by Django 4.0.6 on 2022-11-15 12:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('database', '0006_tarea_usuario_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='plan',
            name='meta_id',
            field=models.ForeignKey(default=12, on_delete=django.db.models.deletion.CASCADE, to='database.meta'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='plan',
            name='usuario_id',
            field=models.ForeignKey(default=2, on_delete=django.db.models.deletion.CASCADE, to='database.usuario'),
            preserve_default=False,
        ),
    ]
