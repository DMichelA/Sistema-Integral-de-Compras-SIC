from django.db import models
from apps.usuario.models import Bienes

prioridades = [
    ('', 'Seleccionar...'),
    ('Normal', 'Normal'),
    ('Urgente', 'Urgente'),
]

proyectos = [
    ('', 'Seleccionar...'),
    ('11 Becas Ing. Prop.', '11 Becas Ing. Prop'),
    ('21 Vinculación', '21 Vinculación'),
    ('22 Extensión Ing. Prop', '22 Extensión Ing. Prop'),
    ('23 Servicio Social', '23 Servicio Social'),
    ('31 Adecuación curricular Ing.Prop', '21 Vinculación'),
    ('32 Material Didáctico', '32 Material Didáctico'),
    ('34 Eval. Desp. Esc. Ing. Prop.', '34 Eval. Desp. Esc. Ing. Prop.'),
    ('35 Atención compensatoria', '35 Atención compensatoria'),
    ('37 Act. Cult., Deport., y Recreat.', '37 Act. Cult., Deport., y Recreat.'),
    ('40 Investigación Ing. Prop.', '40 Investigación Ing. Prop.'),
    ('41  Dif. Institucional Ing. Prop.', '41  Dif. Institucional Ing. Prop.'),
    ('52 Equipamiento', '52 Equipamiento'),
    ('53  Mtto. prev. y correctivo', '53  Mtto. prev. y correctivo'),
    ('62  Admón Central Ing. Prop.', '62  Admón Central Ing. Prop.'),
    ('93  Cap. y Act. de Personal Docente', '93  Cap. y Act. de Personal Docente'),
    ('94 Cap. Y  Act. De Serv. Públicos', '94 Cap. Y  Act. De Serv. Públicos'),
    ('95 Sist. Información', '95 Sist. Información'),
    ('PROMEP', 'PROMEP'),
    ('FAM', 'FAM'),
    ('FAC', 'FAC'),
    ('PROYECTO ESPECIAL', 'PROYECTO ESPECIAL'),
]


class Requisicion(models.Model):
    pagina = models.IntegerField(default=1)
    de = models.IntegerField(default=1)
    fecha_elaboracion = models.DateField()
    periodo = models.CharField(max_length=60)
    folio = models.IntegerField()
    fecha_requerida = models.DateField()
    num_contrato = models.IntegerField()
    prioridad = models.CharField(
        max_length=30, 
        choices=prioridades,
        default='Normal'
    )
    proyecto = models.CharField(max_length=60, choices=proyectos)
    nombre_lider = models.CharField(max_length=60)
    justificacion = models.TextField(null=False, blank=True) 
    bien_servicio = models.ManyToManyField(Bienes, blank=False)
    
    autorizacion_totalgasto = models.DecimalField(max_digits=6, decimal_places=2, null=False, blank=False, default=0)
    max_autorizadoFE = models.DecimalField(max_digits=6, decimal_places=2, null=False, blank=False, default=0)
    max_autorizadoES = models.DecimalField(max_digits=6, decimal_places=2, null=False, blank=False, default=0)
    max_autorizadoIP = models.DecimalField(max_digits=6, decimal_places=2, null=False, blank=False, default=0)
    presupuesto_proyectoFE = models.DecimalField(max_digits=6, decimal_places=2, null=False, blank=False, default=0)
    presupuesto_proyectoES = models.DecimalField(max_digits=6, decimal_places=2, null=False, blank=False, default=0)
    presupuesto_proyectoIP = models.DecimalField(max_digits=6, decimal_places=2, null=False, blank=False, default=0)
    firma_autorizacion = models.CharField(max_length=60, null=False, blank=True)
    observaciones = models.TextField(null=False, blank=True)
    firma_encargadafinanzas = models.CharField(max_length=60, null=False, blank=True)
    firma_rector = models.CharField(max_length=60, null=False, blank=True, default='Mtro. José Antonio Zamora Guido')
    firmas_conformidad = models.CharField(max_length=60, null=False, blank=True)

