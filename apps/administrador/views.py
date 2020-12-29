from django.shortcuts import render,redirect
from django.http import HttpResponse

from apps.usuario.forms import BienesForm
from apps.usuario.models import Bienes
from apps.login.models import User
from django.db.models import Q

# Create your views here.
def index(request):
    return render(request, 'administrador/index.html')

def listado_bienes(request):
    busqueda = request.POST.get("buscar")
    bien = Bienes.objects.all().order_by('id')

    if busqueda:
        bien = Bienes.objects.filter(
            Q(area_solicitante__icontains = busqueda) |
            Q(programa_poa__icontains = busqueda) |
            Q(codigo_partida__icontains = busqueda)
        ).distinct()
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
    busqueda = request.POST.get("buscar")
    bien = Bienes.objects.all().order_by('id')

    if busqueda:
        bien = Bienes.objects.filter(
            Q(area_solicitante__icontains = busqueda) |
            Q(programa_poa__icontains = busqueda) |
            Q(codigo_partida__icontains = busqueda)
        ).distinct()
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


def activar_permisos(request):
    usuario = User.objects.all()
    contexto = {'usuarios':usuario}
    return render(request, 'administrador/permisos.html', contexto)


def actualizar_permiso(request):
    id = request.POST['id']
    activar = request.POST['activar']
    print(activar)
    print(id)
    if activar == 'False':
        obj = User.objects.get(id=id)
        print(obj)
        save = False
        obj.is_staff = True
        obj.save()
        save = True
        if save:
            print('Actualizado')
            return redirect('/administrador/permisos/')
    else:
        obj = User.objects.get(id=id)
        print(obj)
        save = False
        obj.is_staff = False
        obj.save()
        save =  True
        if save:
            print('Actualizado')
            return redirect('/administrador/permisos/')
