from django.shortcuts import render,redirect

from apps.usuario.forms import BienesForm
from apps.usuario.models import Bienes

# Create your views here.
def index(request):
    return render(request, 'administrador/index.html')

def listado_bienes(request):
    bien = Bienes.objects.all().order_by('id')
    contexto = {'bienes':bien}
    return render(request, 'administrador/listado.html', contexto)

def bienes_adjudicar(request, id_bien):
    bien = Bienes.objects.get(id=id_bien)
    if request.method == 'GET':
        form = BienesForm(instance=bien)
    else:
        form = BienesForm(request.POST, instance=bien)
        if form.is_valid():
            form.save()
        return redirect('listado_bienes')
    return render(request, 'administrador/adjudicacion.html', {'form':form})

def bienes_adjudicados(request):
    bien = Bienes.objects.all().order_by('id')
    contexto = {'bienes':bien}
    return render(request, 'administrador/verificados.html', contexto)

def actualizar_bienes(request, id_bien):
    bien = Bienes.objects.get(id=id_bien)
    if request.method == 'GET':
        form = BienesForm(instance=bien)
    else:
        form = BienesForm(request.POST, instance=bien)
        if form.is_valid():
            form.save()
        return redirect('listado_bienes')
    return render(request, 'administrador/actualizacion.html', {'form':form})

def eliminar_bienes(request, id_bien):
    bien = Bienes.objects.get(id=id_bien)
    if request.method == 'GET':
        form = BienesForm(instance=bien)
    else:
        form = BienesForm(request.POST, instance=bien)
        bien.delete()
        return redirect('listado_bienes')
    return render(request, 'administrador/eliminacion.html', {'form':form})