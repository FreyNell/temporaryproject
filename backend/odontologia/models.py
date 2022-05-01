from django.db import models
from django.contrib.auth.models import User

class TipoPerfil(models.Model):
    id_tipo_perfil = models.AutoField(primary_key=True)
    nombre_perfil = models.CharField(max_length=20)

    def __str__(self):
        return self.nombre_perfil

class Perfiles(models.Model):
    usuario = models.OneToOneField(User, on_delete=models.CASCADE)
    tipo_perfil = models.ForeignKey(TipoPerfil, on_delete=models.CASCADE)

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

