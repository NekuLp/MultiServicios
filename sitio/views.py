from django.shortcuts import render
from sitio.models import Noticia,Solicitud
from sitio.forms import SolicitudForm
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required

# Create your views here.
def index(request):
    context_dict = {}
    noticias = Noticia.objects.all().order_by('-fecha')[:3]
    context_dict['noticias'] = noticias
    return render(request, 'index.html', context_dict)

def noticias(request):
    context_dict = {}
    noticias = Noticia.objects.all().order_by('-fecha')
    context_dict['noticias'] = noticias
    return render(request, 'noticias.html', context_dict)

def contacto(request):
    context_dict = {}
    return render(request, 'contacto.html', context_dict)

def conocenos(request):
    context_dict = {}
    return render(request, 'conocenos.html', context_dict)

def servicios(request):
    context_dict = {}
    return render(request, 'servicios.html', context_dict)

def solicitud(request):
    context_dict = {}
    if request.method == "POST":
        form = SolicitudForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('solicitud_enviada')
    else:
        form = SolicitudForm()
    context_dict['form'] = form
    return render(request, 'solicitud.html', context_dict)

def solicitud_enviada(request):
    context_dict = {}
    return render(request, 'solicitudenviada.html', context_dict)

@login_required
def lista_solicitud(request):
    context_dict = {}
    solicitudes = Solicitud.objects.all().order_by('-id')
    context_dict['solicitudes'] = solicitudes
    return render(request, 'lista_solicitudes.html', context_dict)

@login_required
def solicitud_detalles(request, id_solicitud):
    context_dict = {}
    solicitud = Solicitud.objects.get(id=id_solicitud)
    context_dict['solicitud'] = solicitud
    return render(request, 'solicitud_detalles.html', context_dict)

@login_required
def solicitud_eliminar(request, id_solicitud):
    solicitud = Solicitud.objects.get(id=id_solicitud)
    solicitud.delete()
    return lista_solicitud(request)
