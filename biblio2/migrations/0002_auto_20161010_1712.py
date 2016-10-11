# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('biblio2', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Idioma',
            fields=[
                ('ididioma', models.IntegerField(primary_key=True, serialize=False, verbose_name='ID', editable=False)),
                ('nome', models.CharField(max_length=45, verbose_name='Idioma')),
                ('sigla', models.CharField(max_length=4, verbose_name='Sigla')),
            ],
        ),
        migrations.AddField(
            model_name='livro',
            name='dataPublicacao',
            field=models.DateField(verbose_name='Data de Publicacao', blank=True, null=True),
        ),
        migrations.AddField(
            model_name='livro',
            name='paginas',
            field=models.IntegerField(verbose_name='Num. Paginas', blank=True, null=True),
        ),
        migrations.AddField(
            model_name='livro',
            name='subtitulo',
            field=models.CharField(max_length=45, verbose_name='Subtitulo', blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='autor',
            name='idautor',
            field=models.IntegerField(primary_key=True, serialize=False, verbose_name='ID', editable=False),
        ),
        migrations.AlterField(
            model_name='autor',
            name='nome',
            field=models.CharField(max_length=45, verbose_name='Nome', blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='emprestimo',
            name='datadevolucao',
            field=models.DateTimeField(verbose_name='Data Devolucao', blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='emprestimo',
            name='dataemprestimo',
            field=models.DateTimeField(verbose_name='Data Emprestimo', blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='emprestimo',
            name='dataprevista',
            field=models.DateTimeField(verbose_name='Data Prevista de Devolucao', blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='emprestimo',
            name='idemprestimo',
            field=models.IntegerField(primary_key=True, serialize=False, verbose_name='ID', editable=False),
        ),
        migrations.AlterField(
            model_name='emprestimo',
            name='livroid',
            field=models.ForeignKey(verbose_name='Livro', blank=True, to='biblio2.Livro', null=True, db_column='livroid'),
        ),
        migrations.AlterField(
            model_name='emprestimo',
            name='usuarioid',
            field=models.ForeignKey(verbose_name='Usuario', blank=True, to='biblio2.Usuario', null=True, db_column='usuarioid'),
        ),
        migrations.AlterField(
            model_name='livro',
            name='autor',
            field=models.ForeignKey(verbose_name='Autor', blank=True, to='biblio2.Autor', null=True, db_column='autor'),
        ),
        migrations.AlterField(
            model_name='livro',
            name='edicao',
            field=models.CharField(max_length=15, verbose_name='Edicao', blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='livro',
            name='editora',
            field=models.CharField(max_length=45, verbose_name='Editora', blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='livro',
            name='idlivro',
            field=models.AutoField(primary_key=True, serialize=False, verbose_name='ID', editable=False),
        ),
        migrations.AlterField(
            model_name='livro',
            name='isbn',
            field=models.CharField(max_length=20, verbose_name='ISBN', blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='livro',
            name='titulo',
            field=models.CharField(max_length=45, verbose_name='Titulo', blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='idusuario',
            field=models.IntegerField(primary_key=True, serialize=False, verbose_name='ID', editable=False),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='nome',
            field=models.CharField(max_length=95, verbose_name='Nome'),
        ),
        migrations.AddField(
            model_name='livro',
            name='idioma',
            field=models.ForeignKey(verbose_name='Idioma', blank=True, to='biblio2.Idioma', null=True, db_column='idioma'),
        ),
    ]
