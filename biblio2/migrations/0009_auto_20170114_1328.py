# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import tagulous.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ('biblio2', '0008_auto_20161104_1419'),
    ]

    operations = [
        migrations.AlterField(
            model_name='livro',
            name='assunto',
            field=tagulous.models.fields.TagField(_set_tag_meta=True, tree=True, space_delimiter=False, to='biblio2.Assunto', help_text='Digite um ou mais assuntos separados por virgula'),
        ),
    ]
