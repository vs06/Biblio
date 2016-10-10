'''
Created on 09/06/2015

@author: victor.sousa
'''
from django.contrib import admin
from biblio2.models import Autor, Livro, Usuario, Emprestimo
from django.utils.translation import ugettext_lazy

admin.site.site_title = ugettext_lazy('BiblioEclesia')
admin.site.site_header = ugettext_lazy('BiblioEclesia')
admin.site.index_title = ugettext_lazy('BiblioEclesia')

class AutorAdmin(admin.ModelAdmin):
    search_fields=[]
    list_filter=['nome']
    _fields=['nome']
    list_display = _fields
    list_display_links = list_display
admin.site.register(Autor,AutorAdmin)

class LivroAdmin(admin.ModelAdmin):
    search_fields=[]
    list_filter=['titulo','autor','editora','edicao','isbn']
    _fields=['titulo','autor','editora','edicao','isbn']
    list_display = _fields
    list_display_links = list_display
    ordering = ['titulo']
admin.site.register(Livro,LivroAdmin)

class UsuarioAdmin(admin.ModelAdmin):
    search_fields=[]
    list_filter=['nome']
    _fields=['nome']
    list_display = _fields
    list_display_links = list_display
admin.site.register(Usuario,UsuarioAdmin)

class EmprestimoAdmin(admin.ModelAdmin):
    search_fields=[]
    list_filter=['dataemprestimo','dataprevista','datadevolucao','usuarioid','livroid']
    _fields=['dataemprestimo','dataprevista','datadevolucao','usuarioid','livroid']
    list_display = _fields
    list_display_links = list_display
admin.site.register(Emprestimo,EmprestimoAdmin)

