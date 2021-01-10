from django.shortcuts import render, redirect

from apps.requisicion.forms import RequisicionForm
from apps.usuario.models import Bienes

def llenado_requisicion(request):
    if request.method == 'POST':
        form = RequisicionForm(request.POST)
        print(form.errors)
        #print(form)
        if form.is_valid():
            #form.instance.bien_servicio = request.POST.get["bienes"]
            form.save()
            return redirect('usuario_index') #Redirecciona a la pagina index
    else:
        form = RequisicionForm(user=request.user)

    bien = Bienes.objects.filter(validacion='Validado', nombre_responsable=request.user)
    contexto = {'form':form, 'bienes':bien}
    return render(request, 'requisicion/formato.html', contexto)



