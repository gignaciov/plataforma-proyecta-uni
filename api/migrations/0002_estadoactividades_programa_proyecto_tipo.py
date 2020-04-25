# Generated by Django 2.2 on 2020-04-25 20:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='EstadoActividades',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('estado', models.CharField(max_length=50)),
                ('descripcion', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Tipo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo', models.CharField(max_length=50)),
                ('descripcion', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Proyecto',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=150)),
                ('siglas', models.CharField(max_length=10)),
                ('descripcion', models.TextField(default='')),
                ('edicion', models.CharField(max_length=10)),
                ('fecha_inicio', models.DateField(blank=True)),
                ('fecha_fin', models.DateField(blank=True)),
                ('imagen', models.ImageField(blank=True, max_length=255, upload_to='proyectos')),
                ('estado', models.ForeignKey(help_text='Indicar el estado del programa: Activo/Inactivo/Finalizado/Cancelado', on_delete=django.db.models.deletion.CASCADE, to='api.EstadoActividades')),
                ('tipo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.Tipo')),
            ],
        ),
        migrations.CreateModel(
            name='Programa',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=250)),
                ('descripcion', models.TextField(default='')),
                ('imagen', models.ImageField(blank=True, max_length=255, upload_to='programas')),
                ('fecha_inicio', models.DateField(blank=True)),
                ('fecha_fin', models.DateField(blank=True)),
                ('estado', models.ForeignKey(help_text='Indicar el estado del programa: Activo/Inactivo/Finalizado/Cancelado', on_delete=django.db.models.deletion.CASCADE, to='api.EstadoActividades')),
            ],
        ),
    ]