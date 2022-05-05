from django.contrib import admin

from .models import Dientes,Perfiles,Pacientes,TipoDocumento,TipoPerfil,PacientesDientes,Codificaciones,TipoCodificacion,InformeForense

admin.site.register(Dientes)
admin.site.register(Perfiles)
admin.site.register(Pacientes)
admin.site.register(TipoDocumento)
admin.site.register(TipoPerfil)
admin.site.register(PacientesDientes)
admin.site.register(Codificaciones)
admin.site.register(TipoCodificacion)
admin.site.register(InformeForense)
