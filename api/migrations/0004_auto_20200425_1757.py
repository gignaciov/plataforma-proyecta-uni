# Generated by Django 2.2 on 2020-04-25 22:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_auto_20200425_1540'),
    ]

    operations = [
        migrations.RenameField(
            model_name='programa',
            old_name='nombre',
            new_name='nombre_programa',
        ),
        migrations.RenameField(
            model_name='proyecto',
            old_name='nombre',
            new_name='nombre_proyecto',
        ),
        migrations.AddField(
            model_name='proyecto',
            name='nombre_programa',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='api.Programa'),
        ),
    ]
