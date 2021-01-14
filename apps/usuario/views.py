from django.shortcuts import render, redirect

from apps.usuario.forms import BienesForm
from apps.usuario.models import Bienes
from django.contrib.auth.decorators import login_required

@login_required(login_url='/')
def index(request):
    return render(request, 'usuario/index.html')

@login_required(login_url='/')
def bienes_insert(request):
    if request.method == 'POST':
        form = BienesForm(request.POST)
        if form.is_valid():
            form.instance.nombre_responsable = request.user
            form.instance.area_solicitante = request.user.area
            form.save()
        return redirect('listar_bienes') #Redirecciona a la pagina usuario/index
    else:
        form = BienesForm()
    return render(request, 'usuario/insert.html', {'form':form})

@login_required(login_url='/')
def bienes_list(request):
    bien = Bienes.objects.filter(nombre_responsable=request.user).order_by('id')
    contexto = {'bienes':bien}
    return render(request, 'usuario/list.html', contexto)

@login_required(login_url='/')
def bienes_update(request, id_bien):
    bien = Bienes.objects.get(id=id_bien)
    if request.method == 'GET':
        form = BienesForm(instance=bien)
    else:
        form = BienesForm(request.POST, instance=bien)
        if form.is_valid():
            form.save()
        return redirect('listar_bienes')
    return render(request, 'usuario/update.html', {'form':form})

'''
def bienes_delete(request, id_bien):
    bien = Bienes.objects.get(id=id_bien)
    if request.method == 'POST':
        bien.delete()
        return redirect('listar_bienes')
    return render(request, 'usuario/delete.html', {'bien':bien})
'''

@login_required(login_url='/')
def bienes_delete(request, id_bien):
    bien = Bienes.objects.get(id=id_bien)
    if request.method == 'GET':
        form = BienesForm(instance=bien)
    else:
        form = BienesForm(request.POST, instance=bien)
        bien.delete()
        return redirect('listar_bienes')
    return render(request, 'usuario/delete.html', {'form':form})

@login_required(login_url='/')
def bienes_verificados(request):
    bien = Bienes.objects.filter(nombre_responsable=request.user).order_by('id')
    contexto = {'bienes':bien}
    return render(request, 'usuario/verificados.html', contexto)