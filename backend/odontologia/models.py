from django.db import models
from django.contrib.auth.models import User

class TipoPerfil(models.Model):
    id_tipo_perfil = models.AutoField(primary_key=True)
    nombre_perfil = models.CharField(max_length=20)

    def __str__(self):
        return self.nombre_perfil

class TipoDocumento(models.Model):
    id_tipo_documento = models.AutoField(primary_key=True)
    nombre_documento_identidad = models.CharField(max_length=20)

    def __str__(self):
        return self.nombre_documento_identidad

class TipoCodificacion(models.Model):
    id_tipo_codificacion = models.AutoField(primary_key=True)
    tipo_codificacion = models.CharField(max_length=20)
    
    def __str__(self):
        return self.tipo_codificacion

class Dientes(models.Model):
    id_diente = models.AutoField(primary_key=True)
    lado = models.CharField(max_length=20,default="Izquierdo")
    numero_diente = models.IntegerField()
    numero_secundario = models.IntegerField()
    orden = models.CharField(max_length=3,default="999")

    def __str__(self):
        return str(self.numero_diente) + " " + str(self.numero_secundario) + " " + str(self.lado) + " " + self.orden

class Perfiles(models.Model):
    usuario = models.OneToOneField(User, on_delete=models.CASCADE)
    tipo_perfil = models.ForeignKey(TipoPerfil, on_delete=models.CASCADE)

class Codificaciones(models.Model):
    id_codificacion = models.AutoField(primary_key=True)
    acronimo = models.CharField(max_length=3)
    significado = models.CharField(max_length=50)
    tipo_codificacion = models.ForeignKey(TipoCodificacion,on_delete=models.CASCADE)

    def __str__(self):
        return self.acronimo + " " + self.significado

class Pacientes(models.Model):
    id_paciente = models.AutoField(primary_key=True)
    n_documento = models.IntegerField()
    tipo_documento = models.ForeignKey(TipoDocumento,on_delete=models.CASCADE)
    primer_nombre = models.CharField(max_length=20)
    segundo_nombre = models.CharField(max_length=20)
    primer_apellido = models.CharField(max_length=20)
    segundo_apellido = models.CharField(max_length=20)

    def __str__(self):
        return self.primer_apellido + " " + self.primer_nombre

class PacientesDientes(models.Model):
    id_paciente_diente = models.AutoField(primary_key=True)
    id_paciente = models.ForeignKey(Pacientes,on_delete=models.CASCADE)
    id_diente = models.ForeignKey(Dientes, on_delete=models.CASCADE)
    diagnostico = models.ForeignKey(Codificaciones, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.id_paciente.primer_nombre + " " + self.id_paciente.primer_apellido + " " + str(self.id_diente.numero_diente) + " " + self.diagnostico.acronimo
        #return str(self.id_paciente_diente) + " " + str(self.id_paciente.id_paciente) + " " + str(self.id_diente.id_diente) + " " + str(self.diagnostico.id_codificacion)

class InformeForense(models.Model):
    id_informe = models.AutoField(primary_key=True)
    numero_informe_pericial = models.CharField(max_length=20,default="")
    ciudad = models.CharField(max_length=20,default="")
    fecha_hora = models.CharField(max_length=20,default="")
    sexo = models.CharField(max_length=20,default="")
    autoridad_solicitante = models.CharField(max_length=30,default="")
    protocolo_necropsia = models.CharField(max_length=200,default="")
    acta_inspeccion_cadaver = models.CharField(max_length=200,default="")
    motivo_peritacion = models.CharField(max_length=50,default="")
    concepto_solicitado = models.CharField(max_length=100,default="")
    resumen_hechos = models.CharField(max_length=200,default="")
    ejemplos_estudio = models.CharField(max_length=200,default="")
    tecnica_empleada = models.CharField(max_length=200,default="")
    examen_exterior_boca = models.CharField(max_length=200,default="")
    examen_exterior_menton = models.CharField(max_length=200,default="")
    examen_exterior_peribucal = models.CharField(max_length=200,default="")
    examen_interior_mucosa = models.CharField(max_length=200,default="")
    examen_interior_mucogivinal = models.CharField(max_length=200,default="")
    examen_interior_frenillos = models.CharField(max_length=200,default="")
    examen_interior_pisoboca = models.CharField(max_length=200,default="")
    examen_interior_paladarduro = models.CharField(max_length=200,default="")
    examen_interior_paladarblando = models.CharField(max_length=200,default="")
    zona_retromolar = models.CharField(max_length=200,default="")
    examen_tejidos_periodontales = models.CharField(max_length=200,default="")
    examen_tejidos_duros_maxilasuperior_forma = models.CharField(max_length=200,default="")
    examen_tejidos_duros_maxilasuperior_tamano = models.CharField(max_length=200,default="")
    examen_tejidos_duros_maxilasuperior_hallazgos = models.CharField(max_length=200,default="")
    examen_tejidos_duros_maxilainferior_forma = models.CharField(max_length=200,default="")
    examen_tejidos_duros_maxilainferior_tamano = models.CharField(max_length=200,default="")
    examen_tejidos_duros_maxilainferior_hallazgos = models.CharField(max_length=200,default="")
    examen_tejidos_duros_maxilainferior_alveolares = models.CharField(max_length=200,default="")
    perfil_concavo = models.CharField(max_length=200,default="")
    perfil_recto = models.CharField(max_length=200,default="")
    perfil_convexo = models.CharField(max_length=200,default="")
    senales_particulares_odontologicas = models.CharField(max_length=200,default="")
    valoracion_edad = models.CharField(max_length=200,default="")
    observaciones = models.CharField(max_length=200,default="")
    examenes_solicitados = models.CharField(max_length=200,default="")
    analisis_conclusiones = models.CharField(max_length=200,default="")
    nombre_perito = models.CharField(max_length=200,default="")
    profesion_perito = models.CharField(max_length=200,default="")
    paciente = models.ForeignKey(Pacientes,on_delete=models.CASCADE)
    
    

