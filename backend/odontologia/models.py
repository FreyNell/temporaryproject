from django.db import models

class TipoPerfil(model.Models):
    id_tipo_perfil = models.AutoField(primary_key=True)
    nombre_perfil = models.CharField(max_length=20)

class Perfiles(model.Models):
    id_perfil = models.AutoField(primary_key=True)
    usuario = models.CharField(max_length=16)
    contrasena = models.CharField(max_length=20)
    tipo_perfil = models.ForeignKey(TipoPerfil, on_delete=models.CASCADE)

class TipoDocumento(model.Models):
    id_tipo_documento = models.AutoField(primary_key=True)
    nombre_documento_identidad = models.CharField(max_length=20)

class TipoCodificacion(model.Models):
    id_tipo_codificacion = models.AutoField(primary_key=True)
    tipo_codificacion = models.CharField(max_length=20)

class Dientes(model.Models):
    id_diente = models.AutoField(primary_key=True)
    nombre_diente = models.CharField(max_length=20)
    numero_diente = models.IntegerField()

class Codificaciones(model.models):
    id_codificacion = models.AutoField(primary_key=True)
    acronimo = models.CharField(max_length=3)
    significado = models.CharField(max_length=50)
    tipo_codificacion = models.ForeignKey(TipoCodificacion,on_delete=models.CASCADE)

class Pacientes(model.Models):
    id_paciente = models.AutoField(primary_key=True)
    n_documento = models.IntegerField()
    tipo_documento = models.ForeignKey(TipoDocumento,on_delete=models.CASCADE)
    primer_nombre = models.CharField(max_length=20)
    segundo_nombre = models.CharField(max_length=20)
    primer_apellido = models.CharField(max_length=20)
    segundo_apellido = models.CharField(max_length=20)

class PacientesDientes(model.Models):
    id_paciente_diente = models.AutoField(primary_key=True)
    id_paciente = models.ForeignKey(Pacientes,on_delete=models.CASCADE)
    id_diente = models.ForeignKey(Dientes, on_delete=models.CASCADE)
    diagnostico = models.ForeignKey(Codificaciones, on_delete=models.CASCADE)
