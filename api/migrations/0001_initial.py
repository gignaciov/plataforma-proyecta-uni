# Generated by Django 2.2 on 2020-04-14 05:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Proyectino',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('codigoproyecta', models.CharField(max_length=10)),
                ('nombre', models.CharField(max_length=50)),
                ('apellido', models.CharField(max_length=50)),
                ('facultad', models.CharField(max_length=6)),
                ('especialidad', models.CharField(max_length=50)),
            ],
        ),
    ]