# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('biblio2', '0003_auto_20161010_1715'),
    ]

    operations = [
        migrations.CreateModel(
            name='Editora',
            fields=[
                ('ideditora', models.IntegerField(verbose_name='ID', editable=False, primary_key=True, serialize=False)),
                ('nome', models.CharField(verbose_name='Editora', max_length=45)),
            ],
        ),
        migrations.AlterField(
            model_name='livro',
            name='editora',
            field=models.ForeignKey(verbose_name='Editora', db_column='editora', blank=True, null=True, to='biblio2.Editora'),
        ),
    ]
