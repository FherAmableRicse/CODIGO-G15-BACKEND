# Generated by Django 3.2 on 2022-08-20 01:46

import cloudinary.models
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('api', '0002_alter_categoria_table'),
    ]

    operations = [
        migrations.CreateModel(
            name='Miembro',
            fields=[
                ('miembro_id', models.AutoField(primary_key=True, serialize=False)),
                ('miembro_titulo', models.CharField(max_length=200, verbose_name='Titulo')),
                ('miembro_biografia', models.TextField()),
                ('miembro_twitter', models.CharField(max_length=100, verbose_name='Twitter')),
                ('miembro_facebook', models.CharField(max_length=100, verbose_name='Facebook')),
                ('miembro_youtube', models.CharField(max_length=100, verbose_name='Youtube')),
                ('miembro_github', models.CharField(max_length=100, verbose_name='GitHub')),
                ('miembro_sitioweb', models.CharField(max_length=100, verbose_name='Sitio Web')),
                ('miembro_imagen', cloudinary.models.CloudinaryField(default='', max_length=255, verbose_name='image')),
                ('usuario_id', models.OneToOneField(on_delete=django.db.models.deletion.RESTRICT, to=settings.AUTH_USER_MODEL, verbose_name='Usuario')),
            ],
            options={
                'db_table': 'tbl_miembro',
            },
        ),
        migrations.CreateModel(
            name='Curso',
            fields=[
                ('curso_id', models.AutoField(primary_key=True, serialize=False)),
                ('curso_titulo', models.CharField(max_length=255, verbose_name='Titulo')),
                ('curso_descripcion', models.TextField()),
                ('curso_resumen', models.TextField()),
                ('curso_precio', models.DecimalField(decimal_places=2, max_digits=10)),
                ('curso_imagen', cloudinary.models.CloudinaryField(default='', max_length=255, verbose_name='image')),
                ('autor_id', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='api.miembro', verbose_name='Autor')),
            ],
            options={
                'db_table': 'tbl_curso',
            },
        ),
    ]
