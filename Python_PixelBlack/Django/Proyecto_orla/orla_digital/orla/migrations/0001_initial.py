# Generated by Django 3.1.2 on 2020-12-20 18:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Curso',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('num', models.IntegerField(unique=True)),
                ('titulo', models.CharField(max_length=150)),
                ('subtitulo', models.CharField(max_length=150)),
                ('Fecha', models.CharField(max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name='Orla',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('apellidos', models.CharField(max_length=150)),
                ('texto', models.TextField()),
                ('image', models.ImageField(null=True, upload_to='images')),
                ('video', models.FileField(null=True, upload_to='videos')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('estado', models.CharField(choices=[('profe', 'Profesor'), ('alumno', 'Alumno')], default='alumno', max_length=10)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='orla.curso')),
            ],
            options={
                'ordering': ('-created',),
            },
        ),
    ]
