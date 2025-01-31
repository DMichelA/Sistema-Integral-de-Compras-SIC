from django import forms

from apps.requisicion.models import Requisicion
from apps.usuario.models import Bienes

class RequisicionForm(forms.ModelForm):

    class Meta:
        model = Requisicion

        fields = [
            'fecha_elaboracion',
            'periodo',
            'folio',
            'fecha_requerida',
            'num_contrato',
            'prioridad',
            'proyecto',
            'nombre_lider',
            'justificacion',
            # 'bien_servicio',
            'autorizacion_totalgasto',
            'max_autorizadoFE',
            'max_autorizadoES',
            'max_autorizadoIP',
            'presupuesto_proyectoFE',
            'presupuesto_proyectoES',
            'presupuesto_proyectoIP',
            'firma_autorizacion',
            'observaciones',
            'firma_encargadafinanzas',
            'firma_rector',
            'firmas_conformidad'
        ]
        labels = {
            'fecha_elaboracion' : 'Elaboración',
            'periodo' : 'Periodo al que aplica',
            'folio' : 'No. de Folio',
            'fecha_requerida' : "Fecha en la que se requiere el servicio",
            'num_contrato' : 'No. de Contrato',
            'prioridad' : 'Prioridad',
            'proyecto' : 'Proyecto',
            'nombre_lider' : 'Lider del Proyecto',
            'justificacion' : 'Justificación',
            # 'bien_servicio' : 'Clave',
            'autorizacion_totalgasto' : 'Gasto Total',
            'max_autorizadoFE': 'Máximo Autorizado Federal',
            'max_autorizadoES': 'Máximo Autorizado Estatal',
            'max_autorizadoIP': 'Máximo Autorizado Ingresos Propios',
            'presupuesto_proyectoFE': 'Proyecto Federal',
            'presupuesto_proyectoES': 'Proyecto Estatal',
            'presupuesto_proyectoIP': 'Proyecto Ingresos Propios',
            'firma_autorizacion' : 'Firma de Autorización',
            'observaciones' : 'Observaciones',
            'firma_encargadafinanzas' : 'Nombre y Firma de Encargada de Administración y Finanzas',
            'firma_rector' : 'Nombre y  Firma del Rector',
            'firmas_conformidad' : 'Nombre y  Firmas de Conformidad y Fecha'
        }
        widgets = {
            'fecha_elaboracion': forms.DateInput(format=('%Y-%m-%d'), attrs={'class': 'form-control', 'id': 'datepicker', 'type': 'date'}),
            'periodo': forms.TextInput(attrs={'class': 'form-control'}),
            'folio': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Escribe el numero de Folio'}),
            'fecha_requerida': forms.DateInput(format=('%Y-%m-%d'), attrs={'class': 'form-control', 'type': 'date'}),
            'num_contrato': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Escribe el numero de Contrato'}),
            'prioridad': forms.Select(attrs={'class': 'form-control'}),
            'proyecto': forms.Select(attrs={'class': 'form-control'}),
            'nombre_lider': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Escribe el nombre del Lider de proyecto'}),
            'justificacion': forms.Textarea(attrs={'class': 'form-control'}),
            # 'bien_servicio': forms.Select(attrs={'class': 'form-control', 'id': 'nod${nod}', 'onchange': "cambiar('nod${nod}')"}),
            'autorizacion_totalgasto': forms.NumberInput(attrs={'class': 'form-control', 'id': 'total_gasto'}),
            'max_autorizadoFE': forms.NumberInput(attrs={'class': 'form-control'}),
            'max_autorizadoES': forms.NumberInput(attrs={'class': 'form-control'}),
            'max_autorizadoIP': forms.NumberInput(attrs={'class': 'form-control'}),
            'presupuesto_proyectoFE': forms.NumberInput(attrs={'class': 'form-control'}),
            'presupuesto_proyectoES': forms.NumberInput(attrs={'class': 'form-control'}),
            'presupuesto_proyectoIP': forms.NumberInput(attrs={'class': 'form-control'}),
            'firma_autorizacion': forms.TextInput(attrs={'class': 'form-control'}),
            'observaciones': forms.Textarea(attrs={'class': 'form-control'}),
            'firma_encargadafinanzas': forms.TextInput(attrs={'class': 'form-control'}),
            'firma_rector': forms.TextInput(attrs={'class': 'form-control'}),
            'firmas_conformidad': forms.TextInput(attrs={'class': 'form-control'}),
        }

    '''
    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user', None)
        super(RequisicionForm, self).__init__(*args, **kwargs)
        self.fields['bien_servicio'].empty_label ='Selecccionar...'
        self.fields['bien_servicio'].queryset = Bienes.objects.filter(validacion='Validado', nombre_responsable=self.user)
    '''