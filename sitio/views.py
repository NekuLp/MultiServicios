from django.shortcuts import render
from sitio.models import Noticia

# Create your views here.
def index(request):
    context_dict = {}
    noticias = Noticia.objects.all().order_by('-fecha')
    context_dict['noticias'] = noticias
    return render(request, 'index.html', context_dict)

def noticias(request):
    context_dict = {}
    return render(request, 'index.html', context_dict)

def contacto(request):
    context_dict = {}
    return render(request, 'index.html', context_dict)