from django.db import models

class TipoPerfil(model.Models):
    id_tipo_perfil = models.AutoField(primary_key=True)
    nombre_perfil = models.CharField(max_length=200)

class Perfiles(model.Models):
    id_perfil = models.AutoField(primary_key=True)
    usuario = models.CharField(max_length=16)
    contrasena = models.CharField(max_length=20)
    tipo_perfil = models.ForeignKey(TipoPerfil, on_delete=models.CASCADE)
