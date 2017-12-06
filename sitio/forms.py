from django import forms
from sitio.models import Solicitud

class SolicitudForm (forms.ModelForm):

    telefono = forms.CharField(max_length=10,validators=[Solicitud.phone_validator,Solicitud.digit_validator])

    class Meta:
        model = Solicitud
        fields = ['nombre','telefono', 'correo', 'servicio', 'descripcion']




