from django.shortcuts import render,redirect
from .models import Codificaciones, Dientes, Pacientes, PacientesDientes, Perfiles, TipoCodificacion, TipoDocumento
from django.template.defaulttags import register


def armar_contexto_base(user):
    dientes_izquierdos  = Dientes.objects.all().filter(lado__iexact="Izquierdo").order_by('orden')
    dientes_derechos = Dientes.objects.all().filter(lado__iexact="Derecho").order_by('orden')
    tipos_de_documento = TipoDocumento.objects.all()
    tipo_perfil = Perfiles.objects.get(usuario=user)
    codificaciones = Codificaciones.objects.all()
    context = {
        'dientes_izquierdos': dientes_izquierdos,
        'dientes_derechos': dientes_derechos,
        'tipos_de_documento':tipos_de_documento,
        'tipo_perfil': str(tipo_perfil.tipo_perfil),
        'codificaciones': codificaciones,
    }
    return context

def index(request):
    if request.user.is_authenticated:
        context = armar_contexto_base(request.user)
        if context['tipo_perfil'] != "Odontologo":
            return render(request,'odontologia/investigador.html',context)
        return render(request,'odontologia/index.html',context)
    else:
        return redirect('/usuario')

def registrarPaciente(request):
    error_message = ""
    context = armar_contexto_base(request.user)
    q = None
    if 'primer_nombre' in request.POST and 'primer_apellido' in request.POST and 'segundo_apellido' in request.POST and 'n_documento' in request.POST and 'tipo_documento' in request.POST:
        if request.POST['primer_nombre'] != "" and request.POST['primer_apellido'] != "" and request.POST['segundo_apellido'] != "" and request.POST['n_documento'] != "" and request.POST['tipo_documento'] != "": 
            q,context = consultar(request,solo_consultar=True)
            
            if q == None:
                q = Pacientes()
                q.primer_nombre=request.POST['primer_nombre']
                q.segundo_nombre=request.POST['segundo_nombre']
                q.primer_apellido=request.POST['primer_apellido']
                q.segundo_apellido=request.POST['segundo_apellido']
                q.n_documento=request.POST['n_documento']
                q.tipo_documento=TipoDocumento.objects.get(pk=int(request.POST['tipo_documento']))
                q.save()

            if q != None:
                q.primer_nombre=request.POST['primer_nombre']
                q.segundo_nombre=request.POST['segundo_nombre']
                q.primer_apellido=request.POST['primer_apellido']
                q.segundo_apellido=request.POST['segundo_apellido']
                q.n_documento=request.POST['n_documento']
                q.tipo_documento=TipoDocumento.objects.get(pk=int(request.POST['tipo_documento']))
                q.save()

            dientes = Dientes.objects.all()
            id_paciente = q
            for diente in dientes:
                if str(diente.numero_diente) in request.POST and request.POST[str(diente.numero_diente)] != "":
                    diagnosticos = request.POST[str(diente.numero_diente)].split(",")
                    id_diente =  Dientes.objects.get(numero_diente=diente.numero_diente)
                    for diagnostico in diagnosticos:
                        print(diagnostico)
                        id_codificacion = Codificaciones.objects.get(acronimo=diagnostico, tipo_codificacion=TipoCodificacion.objects.all()[0])
                        try:
                            paciente = PacientesDientes.objects.get(id_diente=id_diente,diagnostico=id_codificacion,id_paciente=id_paciente)
                        except PacientesDientes.DoesNotExist:
                            paciente = PacientesDientes()
                            paciente.id_diente = id_diente
                            paciente.id_paciente = id_paciente
                            paciente.diagnostico = id_codificacion 
                            paciente.save()

    
    context['primer_nombre'] = q.primer_nombre
    context['segundo_nombre'] = q.segundo_nombre
    context['primer_apellido'] = q.primer_apellido
    context['segundo_apellido'] = q.segundo_apellido
    context['n_documento'] = q.n_documento
    context['tipo_documento'] = str(q.tipo_documento)
    context['error_message'] = error_message

    return render(request,'odontologia/index.html',context)

def consultar(request, solo_consultar=False):
    q = None
    error_message = ""
    if not solo_consultar:
        if request.POST['tipo_consulta'] == "1":
            # Numero documento
            if 'c_n_documento' in request.POST and request.POST['c_n_documento'] != "" :
                try:
                    q = Pacientes.objects.get(
                        n_documento=request.POST['c_n_documento'],
                    )
                except Pacientes.DoesNotExist:
                    q = None            
                except Pacientes.MultipleObjectsReturned:
                    q = Pacientes.objects.filter(
                        n_documento=request.POST['c_n_documento'],
                    )[0]

        elif request.POST['tipo_consulta'] == "2":
            if 'c_primer_nombre' in request.POST and 'c_primer_apellido' in request.POST and 'c_segundo_apellido' in request.POST and request.POST['c_primer_nombre'] != "" and request.POST['c_primer_apellido'] != "" and request.POST['c_segundo_apellido'] != "":
                try:
                    q = Pacientes.objects.get(
                        primer_nombre=request.POST['c_primer_nombre'],
                        primer_apellido=request.POST['c_primer_apellido'],
                        segundo_apellido=request.POST['c_segundo_apellido'],
                    )
                except Pacientes.DoesNotExist:
                    q = None
                
                except Pacientes.MultipleObjectsReturned:
                    q = Pacientes.objects.filter(
                        primer_nombre=request.POST['c_primer_nombre'],
                        primer_apellido=request.POST['c_primer_apellido'],
                        segundo_apellido=request.POST['c_segundo_apellido'],
                    )[0]
    else:
        if 'n_documento' in request.POST and request.POST['n_documento'] != "" :
            try:
                q = Pacientes.objects.get(
                    n_documento=request.POST['n_documento'],
                )
            except Pacientes.DoesNotExist:
                q = None            
            except Pacientes.MultipleObjectsReturned:
                q = Pacientes.objects.filter(
                    n_documento=request.POST['n_documento'],
                )[0]

    if q != None:
        pass
    else:
        error_message = "Paciente no encontrado."
    
    context = armar_contexto_base(request.user)
    if q != None:
        context['primer_nombre'] = q.primer_nombre
        context['segundo_nombre'] = q.segundo_nombre
        context['primer_apellido'] = q.primer_apellido
        context['segundo_apellido'] = q.segundo_apellido
        context['n_documento'] = q.n_documento
        context['tipo_documento'] = str(q.tipo_documento)
    context['error_message'] = error_message

    data = {}
    if q != None:
        data_raw = PacientesDientes.objects.all().filter(id_paciente=q)
        if data_raw != None:
            for dato in data_raw:
                if dato.id_diente.numero_diente not in data:
                    data[dato.id_diente.numero_diente] = dato.diagnostico.acronimo
                else:
                    data[dato.id_diente.numero_diente] += "," + dato.diagnostico.acronimo

    context['data'] = data
    if not solo_consultar:
        return render(request,'odontologia/index.html',context)
    else:
        return q,context

@register.filter
def get_value(dictionary, key):
    return dictionary.get(key)