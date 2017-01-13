# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('biblio2', '0005_livro_descricao'),
    ]

    operations = [
        migrations.AlterField(
            model_name='livro',
            name='autor',
            field=models.ForeignKey(verbose_name='Autor', default=1, db_column='autor', to='biblio2.Autor'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='livro',
            name='idioma',
            field=models.ForeignKey(verbose_name='Idioma', null=True, default=1, db_column='idioma', blank=True, to='biblio2.Idioma'),
        ),
        migrations.AlterField(
            model_name='livro',
            name='titulo',
            field=models.CharField(verbose_name='Titulo', default='Titulo', max_length=45),
            preserve_default=False,
        ),
    ]
