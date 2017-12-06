from django.core.exceptions import ValidationError
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

class Solicitud(models.Model):

    def phone_validator(value):

        if len(value) < 10:
            raise ValidationError(
                'El número telefónico no puede tener menos de 10 digitos', code='invalid')

    def digit_validator(value):
         if not value.isdigit():
            raise ValidationError('Este campo debe contener unicamente numeros [0-9]', code='invalid')

    servicios=(
        ('Lavado de motor','Lavado de motor'),
        ('Hidro Lavadoras', 'Hidro Lavadoras'),
        ('Compresores', 'Compresores'),
        ('Maquinas de ejercicio', 'Maquinas de ejercicio')
    )

    nombre = models.CharField(blank=False, max_length=50, verbose_name="Nombre" )
    telefono = models.CharField(blank=False,max_length=10, verbose_name="Telefono")
    correo = models.EmailField()
    servicio = models.CharField(max_length=36,choices=servicios, default='Servicio1')
    descripcion = models.CharField(max_length=550, blank=False, verbose_name='Descripción')



