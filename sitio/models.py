from django.db import models

# Create your models here.

class Noticia(models.Model):
    titulo = models.CharField(blank=False, max_length=50)
    contenido = models.TextField(blank=False)
    fecha = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "noticia"
        verbose_name_plural = "noticias"

    def __str__(self):
        return self.titulo
