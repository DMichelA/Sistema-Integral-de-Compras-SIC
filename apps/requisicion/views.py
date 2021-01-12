from django.shortcuts import render, redirect

from apps.requisicion.forms import RequisicionForm
from apps.usuario.models import Bienes
from apps.requisicion.models import Requisicion, Requisicion_Bienes

def llenado_requisicion(request):
    if request.method == 'POST':
        form = RequisicionForm(request.POST)
        print(form.errors)
        # print(form)
        if form.is_valid():
            # form.instance.bien_servicio = request.POST.get["bienes"]
            form.save()
            return redirect('usuario_index') # Redirecciona a la pagina index
    else:
        # form = RequisicionForm(user=request.user)
        form = RequisicionForm()

    bien = Bienes.objects.filter(validacion='Validado', nombre_responsable=request.user)
    contexto = {'form':form, 'bienes':bien}
    return render(request, 'requisicion/formato.html', contexto)

def envio_datos(request):
    if request.method == 'POST':
        print(request.POST)
        datos = request.POST
        r = Requisicion(fecha_elaboracion=datos["fecha_requerida"], periodo=datos["periodo"], folio=datos["folio"], fecha_requerida=datos["fecha_requerida"], num_contrato=datos["num_contrato"], prioridad=datos["prioridad"], proyecto=datos["proyecto"], nombre_lider=datos["nombre_lider"], justificacion=datos["justificacion"], autorizacion_totalgasto=datos["autorizacion_totalgasto"], max_autorizadoFE=datos["max_autorizadoFE"], max_autorizadoES=datos["max_autorizadoES"], max_autorizadoIP=datos["max_autorizadoIP"], presupuesto_proyectoFE=datos["presupuesto_proyectoFE"], presupuesto_proyectoES=datos["presupuesto_proyectoES"], presupuesto_proyectoIP=datos["presupuesto_proyectoIP"], firma_autorizacion=datos["firma_autorizacion"], observaciones=datos["observaciones"], firma_encargadafinanzas=datos["firma_encargadafinanzas"], firma_rector=datos["firma_rector"], firmas_conformidad=datos["firmas_conformidad"] )
        r.save()
        return redirect('usuario_index')

def envio_bienes(request):
    requisicion_ids = Requisicion.objects.all().values_list('pk', flat=True)
    print(requisicion_ids)
    longitud = len(requisicion_ids)
    for i in range (0, longitud):
        if i == longitud-1:
            ultimo = (requisicion_ids[i])+1
            print(ultimo)
    if request.method == 'POST':
        print(request.POST)
        datos = request.POST
        longitud2 = len(datos)
        longitud2 = longitud2-1
        for i in range (0, longitud2):
            print(i)
            posicion = 'id'+str(i)
            print(posicion)
            rb = Requisicion_Bienes(requisicion_id=ultimo, bienes_id=datos[posicion])
            rb.save()
        return redirect('usuario_index')

