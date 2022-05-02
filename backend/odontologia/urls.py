from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('registrarPaciente',views.registrarPaciente,name='registrarPaciente'),
    path('consultar',views.consultar,name='consultar'),
    path('consultar_forense',views.consultar_forense,name='consultar_forense')
]
