# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('biblio2', '0004_auto_20161011_0842'),
    ]

    operations = [
        migrations.AddField(
            model_name='livro',
            name='descricao',
            field=models.TextField(null=True, blank=True, verbose_name='Descricao'),
        ),
    ]
