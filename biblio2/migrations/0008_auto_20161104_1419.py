# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import tagulous.models.fields
import tagulous.models.models


class Migration(migrations.Migration):

    dependencies = [
        ('biblio2', '0007_auto_20161103_1056'),
    ]

    operations = [
        migrations.CreateModel(
            name='Assunto',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('name', models.CharField(max_length=255, unique=True)),
                ('slug', models.SlugField()),
                ('count', models.IntegerField(help_text='Internal counter of how many times this tag is in use', default=0)),
                ('protected', models.BooleanField(help_text='Will not be deleted when the count reaches 0', default=False)),
                ('path', models.TextField(unique=True)),
                ('label', models.CharField(max_length=255, help_text='The name of the tag, without ancestors')),
                ('level', models.IntegerField(help_text='The level of the tag in the tree', default=1)),
                ('parent', models.ForeignKey(blank=True, null=True, to='biblio2.Assunto', related_name='children')),
            ],
            options={
                'abstract': False,
                'ordering': ('name',),
            },
            bases=(tagulous.models.models.BaseTagTreeModel, models.Model),
        ),
        migrations.DeleteModel(
            name='_Tagulous_Livro_tags',
        ),
        migrations.RemoveField(
            model_name='livro',
            name='tags',
        ),
        migrations.AddField(
            model_name='livro',
            name='assunto',
            field=tagulous.models.fields.TagField(space_delimiter=False, help_text='Digite um ou mais assuntos separados por virgula', to='biblio2.Assunto', tree=True, autocomplete_view='livro_assuntos_autocomplete', _set_tag_meta=True),
        ),
        migrations.AlterUniqueTogether(
            name='assunto',
            unique_together=set([('slug', 'parent')]),
        ),
    ]
