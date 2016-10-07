# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Autor',
            fields=[
                ('idautor', models.IntegerField(editable=False, primary_key=True, serialize=False)),
                ('nome', models.CharField(max_length=45, null=True, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Emprestimo',
            fields=[
                ('idemprestimo', models.IntegerField(editable=False, primary_key=True, serialize=False)),
                ('dataemprestimo', models.DateTimeField(null=True, blank=True)),
                ('datadevolucao', models.DateTimeField(null=True, blank=True)),
                ('dataprevista', models.DateTimeField(null=True, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Livro',
            fields=[
                ('idlivro', models.AutoField(editable=False, primary_key=True, serialize=False)),
                ('titulo', models.CharField(max_length=45, null=True, blank=True)),
                ('editora', models.CharField(max_length=45, null=True, blank=True)),
                ('edicao', models.CharField(max_length=15, null=True, blank=True)),
                ('isbn', models.CharField(max_length=20, null=True, blank=True)),
                ('autor', models.ForeignKey(to='biblio2.Autor', null=True, blank=True, db_column='autor')),
            ],
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('idusuario', models.IntegerField(editable=False, primary_key=True, serialize=False)),
                ('nome', models.CharField(max_length=95)),
            ],
        ),
        migrations.AddField(
            model_name='emprestimo',
            name='livroid',
            field=models.ForeignKey(to='biblio2.Livro', null=True, blank=True, db_column='livroid'),
        ),
        migrations.AddField(
            model_name='emprestimo',
            name='usuarioid',
            field=models.ForeignKey(to='biblio2.Usuario', null=True, blank=True, db_column='usuarioid'),
        ),
    ]
