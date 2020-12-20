# Generated by Django 3.1.2 on 2020-12-18 04:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('usuario', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Requisicion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pagina', models.IntegerField(default=1)),
                ('de', models.IntegerField(default=1)),
                ('fecha_elaboracion', models.DateField()),
                ('periodo', models.CharField(max_length=60)),
                ('folio', models.IntegerField()),
                ('fecha_requerida', models.DateField()),
                ('num_contrato', models.IntegerField()),
                ('prioridad', models.CharField(choices=[('', 'Seleccionar...'), ('Normal', 'Normal'), ('Urgente', 'Urgente')], default='Normal', max_length=30)),
                ('proyecto', models.CharField(choices=[('', 'Seleccionar...'), ('11 Becas Ing. Prop.', '11 Becas Ing. Prop'), ('21 Vinculación', '21 Vinculación'), ('22 Extensión Ing. Prop', '22 Extensión Ing. Prop'), ('23 Servicio Social', '23 Servicio Social'), ('31 Adecuación curricular Ing.Prop', '21 Vinculación'), ('32 Material Didáctico', '32 Material Didáctico'), ('34 Eval. Desp. Esc. Ing. Prop.', '34 Eval. Desp. Esc. Ing. Prop.'), ('35 Atención compensatoria', '35 Atención compensatoria'), ('37 Act. Cult., Deport., y Recreat.', '37 Act. Cult., Deport., y Recreat.'), ('40 Investigación Ing. Prop.', '40 Investigación Ing. Prop.'), ('41  Dif. Institucional Ing. Prop.', '41  Dif. Institucional Ing. Prop.'), ('52 Equipamiento', '52 Equipamiento'), ('53  Mtto. prev. y correctivo', '53  Mtto. prev. y correctivo'), ('62  Admón Central Ing. Prop.', '62  Admón Central Ing. Prop.'), ('93  Cap. y Act. de Personal Docente', '93  Cap. y Act. de Personal Docente'), ('94 Cap. Y  Act. De Serv. Públicos', '94 Cap. Y  Act. De Serv. Públicos'), ('95 Sist. Información', '95 Sist. Información'), ('PROMEP', 'PROMEP'), ('FAM', 'FAM'), ('FAC', 'FAC'), ('PROYECTO ESPECIAL', 'PROYECTO ESPECIAL')], max_length=60)),
                ('nombre_lider', models.CharField(max_length=60)),
                ('justificacion', models.TextField(blank=True)),
                ('autorizacion_totalgasto', models.DecimalField(decimal_places=2, default=0, max_digits=6)),
                ('max_autorizadoFE', models.DecimalField(decimal_places=2, default=0, max_digits=6)),
                ('max_autorizadoES', models.DecimalField(decimal_places=2, default=0, max_digits=6)),
                ('max_autorizadoIP', models.DecimalField(decimal_places=2, default=0, max_digits=6)),
                ('presupuesto_proyectoFE', models.DecimalField(decimal_places=2, default=0, max_digits=6)),
                ('presupuesto_proyectoES', models.DecimalField(decimal_places=2, default=0, max_digits=6)),
                ('presupuesto_proyectoIP', models.DecimalField(decimal_places=2, default=0, max_digits=6)),
                ('firma_autorizacion', models.CharField(blank=True, max_length=60)),
                ('observaciones', models.TextField(blank=True)),
                ('firma_encargadafinanzas', models.CharField(blank=True, max_length=60)),
                ('firma_rector', models.CharField(blank=True, default='Mtro. José Antonio Zamora Guido', max_length=60)),
                ('firmas_conformidad', models.CharField(blank=True, max_length=60)),
                ('bien_servicio', models.ManyToManyField(to='usuario.Bienes')),
            ],
        ),
    ]
