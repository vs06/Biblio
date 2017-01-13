# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import tagulous.models.fields
import tagulous.models.models


class Migration(migrations.Migration):

    dependencies = [
        ('biblio2', '0006_auto_20161013_1706'),
    ]

    operations = [
        migrations.CreateModel(
            name='_Tagulous_Livro_tags',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('name', models.CharField(max_length=255, unique=True)),
                ('slug', models.SlugField()),
                ('count', models.IntegerField(default=0, help_text='Internal counter of how many times this tag is in use')),
                ('protected', models.BooleanField(default=False, help_text='Will not be deleted when the count reaches 0')),
            ],
            options={
                'ordering': ('name',),
                'abstract': False,
            },
            bases=(tagulous.models.models.BaseTagModel, models.Model),
        ),
        migrations.AlterField(
            model_name='emprestimo',
            name='dataprevista',
            field=models.DateTimeField(blank=True, verbose_name='Data Prevista de Devolucao', editable=False, null=True),
        ),
        migrations.AlterUniqueTogether(
            name='_tagulous_livro_tags',
            unique_together=set([('slug',)]),
        ),
        migrations.AddField(
            model_name='livro',
            name='tags',
            field=tagulous.models.fields.TagField(force_lowercase=True, to='biblio2._Tagulous_Livro_tags', _set_tag_meta=True, help_text='Enter a comma-separated tag string', max_count=5),
        ),
    ]
