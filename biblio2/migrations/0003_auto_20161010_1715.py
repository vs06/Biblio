# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('biblio2', '0002_auto_20161010_1712'),
    ]

    operations = [
        migrations.AlterField(
            model_name='idioma',
            name='sigla',
            field=models.CharField(max_length=5, verbose_name='Sigla'),
        ),
    ]
