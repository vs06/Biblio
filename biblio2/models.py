# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
#
# Also note: You'll have to insert the output of 'django-admin sqlcustom [app_label]'
# into your database.
from __future__ import unicode_literals

from datetime import timedelta

from django.db import models
import tagulous.models

class Autor(models.Model):
    idautor = models.IntegerField(primary_key=True, editable=False, verbose_name="ID")
    nome = models.CharField(max_length=45, blank=True, null=True, verbose_name="Nome")
    
    def __str__(self):
        return self.nome

class Emprestimo(models.Model):
    idemprestimo = models.IntegerField(primary_key=True, editable=False, verbose_name="ID")
    dataemprestimo = models.DateTimeField(blank=True, null=True, verbose_name="Data Emprestimo")
    datadevolucao = models.DateTimeField(blank=True, null=True, verbose_name="Data Devolucao")
    usuarioid = models.ForeignKey('Usuario', db_column='usuarioid', blank=True, null=True, verbose_name="Usuario")
    livroid = models.ForeignKey('Livro', db_column='livroid', blank=True, null=True, verbose_name="Livro")
    dataprevista = models.DateTimeField(blank=True, null=True, verbose_name="Data Prevista de Devolucao", editable=False)

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        if not self.idemprestimo:
            self.dataprevista = self.dataemprestimo + timedelta(days=14)
        return models.Model.save(self, force_insert=force_insert, force_update=force_update, using=using, update_fields=update_fields)

class Assunto(tagulous.models.TagTreeModel):
    class TagMeta:
        space_delimiter = False
        #autocomplete_view = 'livro_assuntos_autocomplete'

class Livro(models.Model):
    idlivro = models.AutoField(primary_key=True, editable=False, verbose_name="ID")
    titulo = models.CharField(max_length=95, verbose_name="Titulo")
    subtitulo = models.CharField(max_length=95, blank=True, null=True, verbose_name="Subtitulo")
    autor = models.ForeignKey('Autor', db_column='autor', verbose_name="Autor")
    descricao = models.TextField(blank=True, null=True, verbose_name="Descricao")
    paginas = models.IntegerField(blank=True, null=True, verbose_name="Num. Paginas")
    editora = models.ForeignKey('Editora', db_column='editora', blank=True, null=True, verbose_name="Editora")
    edicao = models.CharField(max_length=15, blank=True, null=True, verbose_name="Edicao")
    dataPublicacao = models.DateField(blank=True, null=True, verbose_name="Data de Publicacao")
    isbn = models.CharField(max_length=20, blank=True, null=True, verbose_name="ISBN")
    idioma = models.ForeignKey('Idioma', db_column='idioma', blank=True, null=True, default=1, verbose_name="Idioma")
    #vários autores?
    #palavras chave ou assunto?
    assunto = tagulous.models.TagField(
        Assunto, help_text = 'Digite um ou mais assuntos separados por virgula',
    )
    #    force_lowercase=True,
    #    max_count=5,
    #    space_delimiter = False,
    #    help_text = 'Digite um ou mais assuntos separados por virgula'
    #)
    
    def __str__(self):
        return self.titulo

class Usuario(models.Model):
    idusuario = models.IntegerField(primary_key=True, editable=False, verbose_name="ID")
    nome = models.CharField(max_length=95, verbose_name="Nome")
    
    def __str__(self):
        return self.nome

class Idioma(models.Model):
    ididioma = models.IntegerField(primary_key=True, editable=False, verbose_name="ID")
    nome = models.CharField(max_length=45, verbose_name="Idioma")
    sigla = models.CharField(max_length=5, verbose_name="Sigla")
    
    def __str__(self):
        return self.nome
    
class Editora(models.Model):
    ideditora = models.IntegerField(primary_key=True, editable=False, verbose_name="ID")
    nome = models.CharField(max_length=45, verbose_name="Editora")
    
    def __str__(self):
        return self.nome
