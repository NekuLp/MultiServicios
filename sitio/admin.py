from django.contrib import admin

# Register your models here.
from django import forms
from sitio.models import Noticia
from django.contrib import admin

class NoticiaForm(forms.ModelForm):
    class Meta:
        model = Noticia
        exclude = ('fecha', )

class NoticiaAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'contenido')
    exclude = ('fecha', )
    form = NoticiaForm

admin.site.register(Noticia, NoticiaAdmin)
