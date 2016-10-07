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

from django.db import models


class Autor(models.Model):
    idautor = models.IntegerField(primary_key=True, editable=False)
    nome = models.CharField(max_length=45, blank=True, null=True)
    
    def __str__(self):
        return self.nome

class Emprestimo(models.Model):
    idemprestimo = models.IntegerField(primary_key=True, editable=False)
    dataemprestimo = models.DateTimeField(blank=True, null=True)
    datadevolucao = models.DateTimeField(blank=True, null=True)
    usuarioid = models.ForeignKey('Usuario', db_column='usuarioid', blank=True, null=True)
    livroid = models.ForeignKey('Livro', db_column='livroid', blank=True, null=True)
    dataprevista = models.DateTimeField(blank=True, null=True)


class Livro(models.Model):
    idlivro = models.AutoField(primary_key=True, editable=False)
    titulo = models.CharField(max_length=45, blank=True, null=True)
    autor = models.ForeignKey(Autor, db_column='autor', blank=True, null=True)
    editora = models.CharField(max_length=45, blank=True, null=True)
    edicao = models.CharField(max_length=15, blank=True, null=True)
    isbn = models.CharField(max_length=20, blank=True, null=True)
    
    def __str__(self):
        return self.titulo

class Usuario(models.Model):
    idusuario = models.IntegerField(primary_key=True, editable=False)
    nome = models.CharField(max_length=95)
    
    def __str__(self):
        return self.nome
