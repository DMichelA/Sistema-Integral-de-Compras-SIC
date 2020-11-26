from django.shortcuts import render

from apps.usuario.models import Bienes

# Create your views here.
def index(request):
    return render(request, 'administrador/index.html')

def verificacion_bienes(request):
    bien = Bienes.objects.all().order_by('id')
    contexto = {'bienes':bien}
    return render(request, 'administrador/verificacion.html', contexto)