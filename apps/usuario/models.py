from django.db import models
from apps.login.models import User

ejes = [
    ('', 'Seleccionar...'),
    ('Fortalecer la calidad educativa', 'Fortalecer la calidad educativa'),
    ('Digitalización de procesos', 'Digitalización de procesos'),
    ('Mejora regulatoria', 'Mejora regulatoria'),
    ('Mejora del ambiente institucional', 'Mejora del ambiente institucional')
]

estrategias = [
    ('', 'Seleccionar...'),
    ('Promover el incremento de matrícula', 'Promover el incremento de matrícula'),
    ('Incremento de PTC en cuerpos académicos', 'Incremento de PTC en cuerpos académicos'),
    ('Disminuir la desigualdad', 'Disminuir la desigualdad'),
    ('Certificación y acreditación de procesos', 'Certificación y acreditación de procesos'),
    ('Participación tripartita en el desarrollo profesional de los universitarios', 'Participación tripartita en el desarrollo profesional de los universitarios'),
    ('Desarrollo docente', 'Desarrollo docente'),
    ('Generar herramientas e instrumentos para la consulta de la información', 'Generar herramientas e instrumentos para la consulta de la información'),
    ('Incremento de procesos automatizados', 'Incremento de procesos automatizados'),
    ('Actualizar marco normativo', 'Actualizar marco normativo'),
    ('Mejorar los procesos para el aprovechamiento de los recursos humanos, materiales y financieros', 'Mejorar los procesos para el aprovechamiento de los recursos humanos, materiales y financieros'),
    ('Fortalecer la corresponsabilidad ambiental', 'Fortalecer la corresponsabilidad ambiental'),
    ('Desarrollo del personal administrativo', 'Desarrollo del personal administrativo'),
    ('Fomentar la sana convivencia', 'Fomentar la sana convivencia')
]

proceso_programa = [
    ('', 'Seleccionar...'),
    ('Vinculación', 'Vinculación'),
    ('Gestión y Operación', 'Gestión y Operación'),
    ('Equidad - Grupos Vulnerables', 'Equidad - Grupos Vulnerables'),
    ('Académico', 'Académico'),
    ('Formación Integral', 'Formación Integral'),
    ('Becas', 'Becas'),
    ('Mantenimiento', 'Mantenimiento'),
    ('Captación', 'Captación'),
    ('Tutorías', 'Tutorías')
]

componentes = [
    ('', 'Seleccionar...'),
    ('A001 Extensión y vinculación', 'A001 Extensión y vinculación'),
    ('A002 Formación', 'A002 Formación'),
    ('A005 Investigación', 'A005 Investigación'),
    ('A006 Planeación', 'A006 Planeación'),
    ('A007 Gestión y Operación', 'A007 Gestión y Operación')
]

proyectos = [
    ('', 'Seleccionar...'),
    ('P011 Becas', 'P011 Becas'),
    ('P021 Vinculación', 'P021 Vinculación'),
    ('P022 Extensión', 'P022 Extensión'),
    ('P031 Adecuación Curricular', 'P031 Adecuación Curricular'),
    ('P032 Material Didáctico', 'P032 Material Didáctico'),
    ('P034 Evaluación del Desempeño Escolar', 'P034 Evaluación del Desempeño Escolar'),
    ('P037 Actividades Culturales, Deportivas y Recreativas', 'P037 Actividades Culturales, Deportivas y Recreativas'),
    ('P040 Investigación', 'P040 Investigación'),
    ('P041 Difusión Institucional', 'P041 Difusión Institucional'),
    ('P053 Mantenimiento Preventivo y Correctivo', 'P053 Mantenimiento Preventivo y Correctivo'),
    ('P061 Evaluación Institucional', 'P061 Evaluación Institucional'),
    ('P062 Administración Central', 'P062 Administración Central'),
    ('P064 Útiles Escolares 2020', 'P064 Útiles Escolares 2020'),
    ('P075 Apoyo a Madres Mexicanas Jefas de Familia 2016', 'P075 Apoyo a Madres Mexicanas Jefas de Familia 2016'),
    ('P078 PRODEP', 'P078 PRODEP'),
    ('P082 Apoyo a Madres Mexicanas Jefas de Familia 2017', 'P082 Apoyo a Madres Mexicanas Jefas de Familia 2017'),
    ('P091 Recuperación por Aseguradora', 'P091 Recuperación por Aseguradora'),
    ('P093 Complemento Aportación Estatal 2019', 'P093 Complemento Aportación Estatal 2019'),
    ('P094 Programa de Fortalecimiento de la Calidad Educativa', 'P094 Programa de Fortalecimiento de la Calidad Educativa'),
    ('P095 CYTNOVA 2019', 'P095 CYTNOVA 2019'),
    ('P096 PIEE 2019', 'P096 PIEE 2019'),
    ('P097 PRODEP 2019', 'P097 PRODEP 2019')
]

areas_solicitantes = [
    ('', 'Seleccionar...'),
    ('Actividades Paraescolares', 'Actividades Paraescolares'),
    ('AEI: Energías Renovables', 'AEI: Energías Renovables'),
    ('AEI: Fotónica', 'AEI: Fotónica'),
    ('AEI: Mecatrónica', 'AEI: Mecatrónica'),
    ('AEI: Nanotecnología', 'AEI: Nanotecnología'),
    ('AEI: Procesos Industriales', 'AEI: Procesos Industriales'),
    ('Biblioteca', 'Biblioteca'),
    ('Calidad ', 'Calidad '),
    ('Contaduría', 'Contaduría'),
    ('COORD.  de Criminalística', 'COORD.  de Criminalística'),
    ('COORD. de Salud Reproductiva', 'COORD. de Salud Reproductiva'),
    ('COORD. de Terapia Física', 'COORD. de Terapia Física'),
    ('Desarrollo e Innovación Institucional', 'Desarrollo e Innovación Institucional'),
    ('Desarrollo Institucional', 'Desarrollo Institucional'),
    ('Difusión', 'Difusión'),
    ('DIR. de Vinculación y Extensión', 'DIR. de Vinculación y Extensión'),
    ('Dirección de Admón. y Finanzas', 'Dirección de Admón. y Finanzas'),
    ('Dirección de Enlace Académico', 'Dirección de Enlace Académico'),
    ('Dirección de Planeación', 'Dirección de Planeación'),
    ('ECE', 'ECE'),
    ('Educación Continua', 'Educación Continua'),
    ('GEOS', 'GEOS'),
    ('Gestión Empresarial', 'Gestión Empresarial'),
    ('Idiomas', 'Idiomas'),
    ('Investigación', 'Investigación'),
    ('Jurídico', 'Jurídico'),
    ('Mantenimiento e Instalaciones', 'Mantenimiento e Instalaciones'),
    ('Parque Vehicular', 'Parque Vehicular'),
    ('Presupuesto y Contabilidad', 'Presupuesto y Contabilidad'),
    ('Programación y Presupuesto', 'Programación y Presupuesto'),
    ('Rectoría', 'Rectoría'),
    ('Recursos Humanos', 'Recursos Humanos'),
    ('Recursos Materiales', 'Recursos Materiales'),
    ('Servicios Escolares', 'Servicios Escolares'),
    ('Servicios Estudiantiles', 'Servicios Estudiantiles'),
    ('Servicios Médicos', 'Servicios Médicos'),
    ('Soporte Técnico', 'Soporte Técnico'),
    ('Tecnologías de la Información', 'Tecnologías de la Información'),
    ('Tutorías', 'Tutorías'),
    ('UA de Cuautepec', 'UA de Cuautepec'),
    ('UA de Santa Úrsula', 'UA de Santa Úrsula'),
    ('UDICE', 'UDICE'),
    ('Seguimiento de Egresados', 'Seguimiento de Egresados'),
    ('Movilidad Internacional', 'Movilidad Internacional')
]

capitulos = [
    ('', 'Seleccionar...'),
    (2000, 2000),
    (3000, 3000),
    (5000, 5000)
]

tipo = [
    ('', 'Seleccionar...'),
    ('Bien', 'Bien'),
    ('Servicio', 'Servicio'),
    ('Mobiliario', 'Mobiliario'),
]

unidades_medida = [
    ('', 'Seleccionar...'),
    ('Bolsa', 'Bolsa'),
    ('Caja', 'Caja'),
    ('Certificación', 'Certificación'),
    ('Ciento', 'Ciento'),
    ('Cubeta (19 Lts.)', 'Cubeta (19 Lts.)'),
    ('Curso', 'Curso'),
    ('Galon', 'Galon'),
    ('Juego', 'Juego'),
    ('Kilogramo', 'Kilogramo'),
    ('Kit', 'Kit'),
    ('Litro', 'Litro'),
    ('Lote', 'Lote'),
    ('Metro', 'Metro'),
    ('Millar', 'Millar'),
    ('Paquete', 'Paquete'),
    ('Pieza', 'Pieza'),
    ('Rollo', 'Rollo'),
    ('Servicio', 'Servicio'),
    ('Tambo', 'Tambo'),
]

status_bien = [
    ('Normal', 'Normal'),
    ('Reprogramado', 'Reprogramado'),
    ('Recalendarizado', 'Recalendarizado'),
    ('Actualizado', 'Actualizado'),
]

validacion = [
    ('No validado', 'No validado'),
    ('Validado', 'Validado'),
]

class Partidas(models.Model):
    descripcion = models.CharField(max_length=200)
    def __str__(self):
        return '{}'.format(self.descripcion)


class Bienes(models.Model):
    eje_pide = models.CharField(
        max_length=35, choices=ejes
    )
    estrategia_pide = models.CharField(
        max_length=100, choices=estrategias
    )
    programa_poa = models.CharField(
        max_length=35, choices=proceso_programa
    )
    componente_poa = models.CharField(
        max_length=35, choices=componentes
    )
    proyecto_poa = models.CharField(
        max_length=60, choices=proyectos
    )
    actividad_poa = models.CharField(max_length=60)
    entregable_poa = models.CharField(max_length=60)
    nombre_responsable = models.ForeignKey(User, null=False, blank=False, on_delete=models.CASCADE)
    area_solicitante = models.CharField(
        max_length=45, choices=areas_solicitantes
    )
    descrip_partida = models.ForeignKey(Partidas, null=False, blank=False, on_delete=models.CASCADE)
    codigo_partida = models.IntegerField()
    codigo_pestatal = models.IntegerField()
    descrip_general_bien = models.CharField(max_length=60, null=False, blank=True, default='Sin descripción') # Null False el formulario no requiere un valor, pero la base de datos sí. 
    espeficaciones_tecnicas = models.CharField(max_length=60, null=False, blank=True)
    capitulo = models.IntegerField(
        null=False, blank=False,
        choices=capitulos
    )
    tipo = models.CharField(
        # default='Unspecified', Desaparece la opcion None '----'
        max_length=15, 
        choices=tipo
    )
    unidad_medida = models.CharField(
        max_length=35, choices=unidades_medida
    )
    cantidad_bienes = models.IntegerField()
    precio_unitario = models.DecimalField(max_digits=10, decimal_places=2)
    total = models.DecimalField(max_digits=10, decimal_places=2)
    ingresos_propios = models.DecimalField(max_digits=10, decimal_places=2, null=False, blank=False, default=0) 
    recurso_fiscal = models.DecimalField(max_digits=10, decimal_places=2, null=False, blank=False, default=0)
    recurso_federal = models.DecimalField(max_digits=10, decimal_places=2, null=False, blank=False, default=0)
    presupues_total_anual = models.DecimalField(max_digits=10, decimal_places=2, null=False, blank=False, default=0)
    licitacion_publica = models.DecimalField(max_digits=10, decimal_places=2, null=False, blank=False, default=0)
    invitacion_personas = models.DecimalField(max_digits=10, decimal_places=2, null=False, blank=False, default=0)
    adjudicacion_directa = models.DecimalField(max_digits=10, decimal_places=2, null=False, blank=False, default=0)
    partidas_paaays = models.DecimalField(max_digits=10, decimal_places=2, null=False, blank=False, default=0)
    cal_enero = models.DecimalField(max_digits=10, decimal_places=2, null=False, blank=False, default=0)
    cal_febrero = models.DecimalField(max_digits=10, decimal_places=2, null=False, blank=False, default=0)
    cal_marzo = models.DecimalField(max_digits=10, decimal_places=2, null=False, blank=False, default=0)
    cal_abril = models.DecimalField(max_digits=10, decimal_places=2, null=False, blank=False, default=0)
    cal_mayo = models.DecimalField(max_digits=10, decimal_places=2, null=False, blank=False, default=0)
    cal_junio = models.DecimalField(max_digits=10, decimal_places=2, null=False, blank=False, default=0)
    cal_julio = models.DecimalField(max_digits=10, decimal_places=2, null=False, blank=False, default=0)
    cal_agosto = models.DecimalField(max_digits=10, decimal_places=2, null=False, blank=False, default=0)
    cal_septiembre = models.DecimalField(max_digits=10, decimal_places=2, null=False, blank=False, default=0)
    cal_octubre = models.DecimalField(max_digits=10, decimal_places=2, null=False, blank=False, default=0)
    cal_noviembre = models.DecimalField(max_digits=10, decimal_places=2, null=False, blank=False, default=0)
    cal_diciembre = models.DecimalField(max_digits=10, decimal_places=2,null=False, blank=False, default=0)
    status = models.CharField(
        max_length=30, 
        choices=status_bien,
        default='Normal'
    )
    fecha_solicitud = models.DateField(auto_now_add=True)
    validacion = models.CharField(
        max_length=15,
        choices=validacion,
        default='No validado'
    )