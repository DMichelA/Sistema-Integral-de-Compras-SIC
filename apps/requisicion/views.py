from django.shortcuts import render, redirect

from apps.requisicion.forms import RequisicionForm

def llenado_requisicion(request):
    if request.method == 'POST':
        form = RequisicionForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('index_usuario') #Redirecciona a la pagina index
    else:
        form = RequisicionForm()
    return render(request, 'requisicion/formato.html', {'form':form})


#TODO Traer datos de la tabla
#TODO Almacenar las requisiciones
#TODO Historial Requisiciones
