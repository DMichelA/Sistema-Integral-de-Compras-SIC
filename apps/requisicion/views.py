from django.shortcuts import render, redirect
from django.db import connection

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
        r = Requisicion(nombre_responsable=request.user, area_solicitante = request.user.area, fecha_elaboracion=datos["fecha_elaboracion"], periodo=datos["periodo"], folio=datos["folio"], fecha_requerida=datos["fecha_requerida"], num_contrato=datos["num_contrato"], prioridad=datos["prioridad"], proyecto=datos["proyecto"], nombre_lider=datos["nombre_lider"], justificacion=datos["justificacion"], autorizacion_totalgasto=datos["autorizacion_totalgasto"], max_autorizadoFE=datos["max_autorizadoFE"], max_autorizadoES=datos["max_autorizadoES"], max_autorizadoIP=datos["max_autorizadoIP"], presupuesto_proyectoFE=datos["presupuesto_proyectoFE"], presupuesto_proyectoES=datos["presupuesto_proyectoES"], presupuesto_proyectoIP=datos["presupuesto_proyectoIP"], firma_autorizacion=datos["firma_autorizacion"], observaciones=datos["observaciones"], firma_encargadafinanzas=datos["firma_encargadafinanzas"], firma_rector=datos["firma_rector"], firmas_conformidad=datos["firmas_conformidad"] )
        r.save()
        return redirect('usuario_index')

def envio_bienes(request):
    requisicion_ids = Requisicion.objects.all().values_list('pk', flat=True)
    print(requisicion_ids)
    longitud = len(requisicion_ids)
    print(longitud)
    if longitud == 0 or longitud == 1:
        ultimo=1
    else:
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

def requisiciones_list(request):
    requisicion = Requisicion.objects.filter(nombre_responsable=request.user).order_by('id')
    contexto = {'requisiciones':requisicion}
    return render(request, 'requisicion/list.html', contexto)

def requisiciones_listado_admin(request):
    requisicion = Requisicion.objects.all().order_by('id')
    contexto = {'requisiciones':requisicion}
    return render(request, 'requisicion/list_admin.html', contexto)

def requisicion_save(request, id_requisicion):
    requisicion = Requisicion.objects.get(id=id_requisicion)
    cursor = connection.cursor()
    cursor.execute("SELECT b.id, b.codigo_partida, b.cantidad_bienes, b.unidad_medida, b.descrip_general_bien, b.espeficaciones_tecnicas, b.precio_unitario, b.total FROM usuario_bienes AS b INNER JOIN requisicion_requisicion_bienes AS rb ON b.id = rb.bienes_id INNER JOIN requisicion_requisicion as r ON rb.requisicion_id = r.id WHERE rb.requisicion_id=%s;", [id_requisicion])
    bien = cursor.fetchall()
    columns = [col[0] for col in cursor.description]
    rows = [dict(zip(columns, row)) for row in bien]
    print(rows)
    if request.method == 'GET':
        form = RequisicionForm(instance=requisicion)
    contexto = {'form':form, 'bienes':rows}
    return render(request, 'requisicion/descargar.html', contexto)

def requisicion_download(request, id_requisicion):
    requisicion = Requisicion.objects.get(id=id_requisicion)
    cursor = connection.cursor()
    cursor.execute("SELECT b.id, b.codigo_partida, b.cantidad_bienes, b.unidad_medida, b.descrip_general_bien, b.espeficaciones_tecnicas, b.precio_unitario, b.total FROM usuario_bienes AS b INNER JOIN requisicion_requisicion_bienes AS rb ON b.id = rb.bienes_id INNER JOIN requisicion_requisicion as r ON rb.requisicion_id = r.id WHERE rb.requisicion_id=%s;", [id_requisicion])
    bien = cursor.fetchall()
    columns = [col[0] for col in cursor.description]
    rows = [dict(zip(columns, row)) for row in bien]
    print(rows)
    if request.method == 'GET':
        form = RequisicionForm(instance=requisicion)
    contexto = {'form':form, 'bienes':rows}
    return render(request, 'requisicion/descargar_admin.html', contexto)