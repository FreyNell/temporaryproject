from django.shortcuts import render,redirect
from .models import Codificaciones, Dientes, Pacientes, PacientesDientes, Perfiles, TipoCodificacion, TipoDocumento, InformeForense
from django.template.defaulttags import register
from django.forms import ModelForm,TextInput

class PeritoForm(ModelForm):
    class Meta:
        model = InformeForense
        fields = [
            'numero_informe_pericial',
            'ciudad',
            'fecha_hora',
            'sexo',
            'autoridad_solicitante',
            'protocolo_necropsia',
            'acta_inspeccion_cadaver',
            'motivo_peritacion',
            'concepto_solicitado',
            'resumen_hechos',
            'ejemplos_estudio',
            'tecnica_empleada',
            'examen_exterior_boca',
            'examen_exterior_menton',
            'examen_exterior_peribucal',
            'examen_interior_mucosa',
            'examen_interior_mucogivinal',
            'examen_interior_frenillos',
            'examen_interior_pisoboca',
            'examen_interior_paladarduro',
            'examen_interior_paladarblando',
            'zona_retromolar',
            'examen_tejidos_periodontales',
            'examen_tejidos_duros_maxilasuperior_forma',
            'examen_tejidos_duros_maxilasuperior_tamano',
            'examen_tejidos_duros_maxilasuperior_hallazgos',
            'examen_tejidos_duros_maxilainferior_forma',
            'examen_tejidos_duros_maxilainferior_tamano',
            'examen_tejidos_duros_maxilainferior_hallazgos',
            'examen_tejidos_duros_maxilainferior_alveolares',
            'perfil_concavo',
            'perfil_recto',
            'perfil_convexo',
            'senales_particulares_odontologicas',
            'valoracion_edad',
            'observaciones',
            'examenes_solicitados',
            'analisis_conclusiones',
            'nombre_perito',
            'profesion_perito',
        ]
        widgets = {
            'numero_informe_pericial': TextInput(attrs={'class': 'form-control'}),
            'ciudad': TextInput(attrs={'class': 'form-control'}),
            'fecha_hora': TextInput(attrs={'class': 'form-control'}),
            'sexo': TextInput(attrs={'class': 'form-control'}),
            'autoridad_solicitante': TextInput(attrs={'class': 'form-control'}),
            'protocolo_necropsia': TextInput(attrs={'class': 'form-control'}),
            'acta_inspeccion_cadaver': TextInput(attrs={'class': 'form-control'}),
            'motivo_peritacion': TextInput(attrs={'class': 'form-control'}),
            'concepto_solicitado': TextInput(attrs={'class': 'form-control'}),
            'resumen_hechos': TextInput(attrs={'class': 'form-control'}),
            'ejemplos_estudio': TextInput(attrs={'class': 'form-control'}),
            'tecnica_empleada': TextInput(attrs={'class': 'form-control'}),
            'examen_exterior_boca': TextInput(attrs={'class': 'form-control'}),
            'examen_exterior_menton': TextInput(attrs={'class': 'form-control'}),
            'examen_exterior_peribucal': TextInput(attrs={'class': 'form-control'}),
            'examen_interior_mucosa': TextInput(attrs={'class': 'form-control'}),
            'examen_interior_mucogivinal': TextInput(attrs={'class': 'form-control'}),
            'examen_interior_frenillos': TextInput(attrs={'class': 'form-control'}),
            'examen_interior_pisoboca': TextInput(attrs={'class': 'form-control'}),
            'examen_interior_paladarduro': TextInput(attrs={'class': 'form-control'}),
            'examen_interior_paladarblando': TextInput(attrs={'class': 'form-control'}),
            'zona_retromolar': TextInput(attrs={'class': 'form-control'}),
            'examen_tejidos_periodontales': TextInput(attrs={'class': 'form-control'}),
            'examen_tejidos_duros_maxilasuperior_forma': TextInput(attrs={'class': 'form-control'}),
            'examen_tejidos_duros_maxilasuperior_tamano': TextInput(attrs={'class': 'form-control'}),
            'examen_tejidos_duros_maxilasuperior_hallazgos': TextInput(attrs={'class': 'form-control'}),
            'examen_tejidos_duros_maxilainferior_forma': TextInput(attrs={'class': 'form-control'}),
            'examen_tejidos_duros_maxilainferior_tamano': TextInput(attrs={'class': 'form-control'}),
            'examen_tejidos_duros_maxilainferior_hallazgos': TextInput(attrs={'class': 'form-control'}),
            'examen_tejidos_duros_maxilainferior_alveolares': TextInput(attrs={'class': 'form-control'}),
            'perfil_concavo': TextInput(attrs={'class': 'form-control'}),
            'perfil_recto': TextInput(attrs={'class': 'form-control'}),
            'perfil_convexo': TextInput(attrs={'class': 'form-control'}),
            'senales_particulares_odontologicas': TextInput(attrs={'class': 'form-control'}),
            'valoracion_edad': TextInput(attrs={'class': 'form-control'}),
            'observaciones': TextInput(attrs={'class': 'form-control'}),
            'examenes_solicitados': TextInput(attrs={'class': 'form-control'}),
            'analisis_conclusiones': TextInput(attrs={'class': 'form-control'}),
            'nombre_perito': TextInput(attrs={'class': 'form-control'}),
            'profesion_perito': TextInput(attrs={'class': 'form-control'}),
        }

def armar_contexto_base(user):
    if not user.is_authenticated:
        return redirect('/')
    
    dientes_izquierdos  = Dientes.objects.all().filter(lado__iexact="Izquierdo").order_by('orden')
    dientes_derechos = Dientes.objects.all().filter(lado__iexact="Derecho").order_by('orden')
    tipos_de_documento = TipoDocumento.objects.all()
    try:
        tipo_perfil = Perfiles.objects.get(usuario=user)
    except Perfiles.DoesNotExist:
        return redirect('/usuario/logout')
    codificaciones = Codificaciones.objects.filter(tipo_codificacion=TipoCodificacion.objects.all()[0])
    codificaciones2 = Codificaciones.objects.filter(tipo_codificacion=TipoCodificacion.objects.all()[1])
    context = {
        'dientes_izquierdos': dientes_izquierdos,
        'dientes_derechos': dientes_derechos,
        'tipos_de_documento':tipos_de_documento,
        'tipo_perfil': str(tipo_perfil.tipo_perfil),
        'codificaciones': codificaciones,
        'codificaciones2': codificaciones2,
    }
    return context

def index(request):
    if request.user.is_authenticated:
        context = armar_contexto_base(request.user)
        return render(request,'odontologia/index.html',context)
    else:
        return redirect('/usuario')

def registrarPaciente(request):
    context = armar_contexto_base(request.user)
    if request.user.is_authenticated and context['tipo_perfil'] == "Odontologo":
        error_message = ""
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
                            id_codificacion = Codificaciones.objects.get(acronimo=diagnostico)
                            try:
                                paciente = PacientesDientes.objects.get(id_diente=id_diente,diagnostico=id_codificacion,id_paciente=id_paciente)
                            except PacientesDientes.DoesNotExist:
                                paciente = PacientesDientes()
                                paciente.id_diente = id_diente
                                paciente.id_paciente = id_paciente
                                paciente.diagnostico = id_codificacion 
                                paciente.save()
                
                evalInforme(request,q)

        
        context['primer_nombre'] = q.primer_nombre
        context['segundo_nombre'] = q.segundo_nombre
        context['primer_apellido'] = q.primer_apellido
        context['segundo_apellido'] = q.segundo_apellido
        context['n_documento'] = q.n_documento
        context['tipo_documento'] = str(q.tipo_documento)
        context['error_message'] = error_message


        context['numero_informe_pericial'] = request.POST.get('numero_informe_pericial','')
        context['ciudad'] = request.POST.get('ciudad','')
        context['fecha_hora'] = request.POST.get('fecha_hora','')
        context['sexo'] = request.POST.get('sexo','')
        context['autoridad_solicitante'] = request.POST.get('autoridad_solicitante','')
        context['protocolo_necropsia'] = request.POST.get('protocolo_necropsia','')
        context['acta_inspeccion_cadaver'] = request.POST.get('acta_inspeccion_cadaver','')
        context['motivo_peritacion'] = request.POST.get('motivo_peritacion','')
        context['concepto_solicitado'] = request.POST.get('concepto_solicitado','')
        context['resumen_hechos'] = request.POST.get('resumen_hechos','')
        context['ejemplos_estudio'] = request.POST.get('ejemplos_estudio','')
        context['tecnica_empleada'] = request.POST.get('tecnica_empleada','')
        context['examen_exterior_boca'] = request.POST.get('examen_exterior_boca','')
        context['examen_exterior_menton'] = request.POST.get('examen_exterior_menton','')
        context['examen_exterior_peribucal'] = request.POST.get('examen_exterior_peribucal','')
        context['examen_interior_mucosa'] = request.POST.get('examen_interior_mucosa','')
        context['examen_interior_mucogivinal'] = request.POST.get('examen_interior_mucogivinal','')
        context['examen_interior_frenillos'] = request.POST.get('examen_interior_frenillos','')
        context['examen_interior_pisoboca'] = request.POST.get('examen_interior_pisoboca','')
        context['examen_interior_paladarduro'] = request.POST.get('examen_interior_paladarduro','')
        context['examen_interior_paladarblando'] = request.POST.get('examen_interior_paladarblando','')
        context['zona_retromolar'] = request.POST.get('zona_retromolar','')
        context['examen_tejidos_periodontales'] = request.POST.get('examen_tejidos_periodontales','')
        context['examen_tejidos_duros_maxilasuperior_forma'] = request.POST.get('examen_tejidos_duros_maxilasuperior_forma','')
        context['examen_tejidos_duros_maxilasuperior_tamano'] = request.POST.get('examen_tejidos_duros_maxilasuperior_tamano','')
        context['examen_tejidos_duros_maxilasuperior_hallazgos'] = request.POST.get('examen_tejidos_duros_maxilasuperior_hallazgos','')
        context['examen_tejidos_duros_maxilainferior_forma'] = request.POST.get('examen_tejidos_duros_maxilainferior_forma','')
        context['examen_tejidos_duros_maxilainferior_tamano'] = request.POST.get('examen_tejidos_duros_maxilainferior_tamano','')
        context['examen_tejidos_duros_maxilainferior_hallazgos'] = request.POST.get('examen_tejidos_duros_maxilainferior_hallazgos','')
        context['examen_tejidos_duros_maxilainferior_alveolares'] = request.POST.get('examen_tejidos_duros_maxilainferior_alveolares','')
        context['perfil_concavo'] = request.POST.get('perfil_concavo','')
        context['perfil_recto'] = request.POST.get('perfil_recto','')
        context['perfil_convexo'] = request.POST.get('perfil_convexo','')
        context['senales_particulares_odontologicas'] = request.POST.get('senales_particulares_odontologicas','')
        context['valoracion_edad'] = request.POST.get('valoracion_edad','')
        context['observaciones'] = request.POST.get('observaciones','')
        context['examenes_solicitados'] = request.POST.get('examenes_solicitados','')
        context['analisis_conclusiones'] = request.POST.get('analisis_conclusiones','')
        context['nombre_perito'] = request.POST.get('nombre_perito','')
        context['profesion_perito'] = request.POST.get('profesion_perito','')

        return render(request,'odontologia/index.html',context)
    else:
        return redirect('/usuario')

def evalInforme(request,paciente):
    try:
        informe = InformeForense.objects.get(paciente=paciente)
        informe.numero_informe_pericial = request.POST.get('numero_informe_pericial','')
        informe.ciudad = request.POST.get('ciudad','')
        informe.fecha_hora = request.POST.get('fecha_hora','')
        informe.sexo = request.POST.get('sexo','')
        informe.autoridad_solicitante = request.POST.get('autoridad_solicitante','')
        informe.protocolo_necropsia = request.POST.get('protocolo_necropsia','')
        informe.acta_inspeccion_cadaver = request.POST.get('acta_inspeccion_cadaver','')
        informe.motivo_peritacion = request.POST.get('motivo_peritacion','')
        informe.concepto_solicitado = request.POST.get('concepto_solicitado','')
        informe.resumen_hechos = request.POST.get('resumen_hechos','')
        informe.ejemplos_estudio = request.POST.get('ejemplos_estudio','')
        informe.tecnica_empleada = request.POST.get('tecnica_empleada','')
        informe.examen_exterior_boca = request.POST.get('examen_exterior_boca','')
        informe.examen_exterior_menton = request.POST.get('examen_exterior_menton','')
        informe.examen_exterior_peribucal = request.POST.get('examen_exterior_peribucal','')
        informe.examen_interior_mucosa = request.POST.get('examen_interior_mucosa','')
        informe.examen_interior_mucogivinal = request.POST.get('examen_interior_mucogivinal','')
        informe.examen_interior_frenillos = request.POST.get('examen_interior_frenillos','')
        informe.examen_interior_pisoboca = request.POST.get('examen_interior_pisoboca','')
        informe.examen_interior_paladarduro = request.POST.get('examen_interior_paladarduro','')
        informe.examen_interior_paladarblando = request.POST.get('examen_interior_paladarblando','')
        informe.zona_retromolar = request.POST.get('zona_retromolar','')
        informe.examen_tejidos_periodontales = request.POST.get('examen_tejidos_periodontales','')
        informe.examen_tejidos_duros_maxilasuperior_forma = request.POST.get('examen_tejidos_duros_maxilasuperior_forma','')
        informe.examen_tejidos_duros_maxilasuperior_tamano = request.POST.get('examen_tejidos_duros_maxilasuperior_tamano','')
        informe.examen_tejidos_duros_maxilasuperior_hallazgos = request.POST.get('examen_tejidos_duros_maxilasuperior_hallazgos','')
        informe.examen_tejidos_duros_maxilainferior_forma = request.POST.get('examen_tejidos_duros_maxilainferior_forma','')
        informe.examen_tejidos_duros_maxilainferior_tamano = request.POST.get('examen_tejidos_duros_maxilainferior_tamano','')
        informe.examen_tejidos_duros_maxilainferior_hallazgos = request.POST.get('examen_tejidos_duros_maxilainferior_hallazgos','')
        informe.examen_tejidos_duros_maxilainferior_alveolares = request.POST.get('examen_tejidos_duros_maxilainferior_alveolares','')
        informe.perfil_concavo = request.POST.get('perfil_concavo','')
        informe.perfil_recto = request.POST.get('perfil_recto','')
        informe.perfil_convexo = request.POST.get('perfil_convexo','')
        informe.senales_particulares_odontologicas = request.POST.get('senales_particulares_odontologicas','')
        informe.valoracion_edad = request.POST.get('valoracion_edad','')
        informe.observaciones = request.POST.get('observaciones','')
        informe.examenes_solicitados = request.POST.get('examenes_solicitados','')
        informe.analisis_conclusiones = request.POST.get('analisis_conclusiones','')
        informe.nombre_perito = request.POST.get('nombre_perito','')
        informe.profesion_perito = request.POST.get('profesion_perito','')
        informe.paciente = paciente
        informe.save()
    except InformeForense.DoesNotExist:
        informe = InformeForense()
        informe.numero_informe_pericial = request.POST.get('numero_informe_pericial','')
        informe.ciudad = request.POST.get('ciudad','')
        informe.fecha_hora = request.POST.get('fecha_hora','')
        informe.sexo = request.POST.get('sexo','')
        informe.autoridad_solicitante = request.POST.get('autoridad_solicitante','')
        informe.protocolo_necropsia = request.POST.get('protocolo_necropsia','')
        informe.acta_inspeccion_cadaver = request.POST.get('acta_inspeccion_cadaver','')
        informe.motivo_peritacion = request.POST.get('motivo_peritacion','')
        informe.concepto_solicitado = request.POST.get('concepto_solicitado','')
        informe.resumen_hechos = request.POST.get('resumen_hechos','')
        informe.ejemplos_estudio = request.POST.get('ejemplos_estudio','')
        informe.tecnica_empleada = request.POST.get('tecnica_empleada','')
        informe.examen_exterior_boca = request.POST.get('examen_exterior_boca','')
        informe.examen_exterior_menton = request.POST.get('examen_exterior_menton','')
        informe.examen_exterior_peribucal = request.POST.get('examen_exterior_peribucal','')
        informe.examen_interior_mucosa = request.POST.get('examen_interior_mucosa','')
        informe.examen_interior_mucogivinal = request.POST.get('examen_interior_mucogivinal','')
        informe.examen_interior_frenillos = request.POST.get('examen_interior_frenillos','')
        informe.examen_interior_pisoboca = request.POST.get('examen_interior_pisoboca','')
        informe.examen_interior_paladarduro = request.POST.get('examen_interior_paladarduro','')
        informe.examen_interior_paladarblando = request.POST.get('examen_interior_paladarblando','')
        informe.zona_retromolar = request.POST.get('zona_retromolar','')
        informe.examen_tejidos_periodontales = request.POST.get('examen_tejidos_periodontales','')
        informe.examen_tejidos_duros_maxilasuperior_forma = request.POST.get('examen_tejidos_duros_maxilasuperior_forma','')
        informe.examen_tejidos_duros_maxilasuperior_tamano = request.POST.get('examen_tejidos_duros_maxilasuperior_tamano','')
        informe.examen_tejidos_duros_maxilasuperior_hallazgos = request.POST.get('examen_tejidos_duros_maxilasuperior_hallazgos','')
        informe.examen_tejidos_duros_maxilainferior_forma = request.POST.get('examen_tejidos_duros_maxilainferior_forma','')
        informe.examen_tejidos_duros_maxilainferior_tamano = request.POST.get('examen_tejidos_duros_maxilainferior_tamano','')
        informe.examen_tejidos_duros_maxilainferior_hallazgos = request.POST.get('examen_tejidos_duros_maxilainferior_hallazgos','')
        informe.examen_tejidos_duros_maxilainferior_alveolares = request.POST.get('examen_tejidos_duros_maxilainferior_alveolares','')
        informe.perfil_concavo = request.POST.get('perfil_concavo','')
        informe.perfil_recto = request.POST.get('perfil_recto','')
        informe.perfil_convexo = request.POST.get('perfil_convexo','')
        informe.senales_particulares_odontologicas = request.POST.get('senales_particulares_odontologicas','')
        informe.valoracion_edad = request.POST.get('valoracion_edad','')
        informe.observaciones = request.POST.get('observaciones','')
        informe.examenes_solicitados = request.POST.get('examenes_solicitados','')
        informe.analisis_conclusiones = request.POST.get('analisis_conclusiones','')
        informe.nombre_perito = request.POST.get('nombre_perito','')
        informe.profesion_perito = request.POST.get('profesion_perito','')
        informe.paciente = paciente
        informe.save()
    
    return informe

def consultar(request, solo_consultar=False):
    if request.user.is_authenticated:
        q = None
        error_message = ""
        if not solo_consultar:            
            if 'tipo_consulta' in request.POST and request.POST['tipo_consulta'] == "1":
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

            elif 'tipo_consulta' in request.POST and request.POST['tipo_consulta'] == "2":
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
        
        if q != None:
            try:
                informe = InformeForense.objects.get(paciente=q)
                print(informe)
                context['numero_informe_pericial'] = informe.numero_informe_pericial
                context['ciudad'] = informe.ciudad
                context['fecha_hora'] = informe.fecha_hora
                context['sexo'] = informe.sexo
                context['autoridad_solicitante'] = informe.autoridad_solicitante
                context['protocolo_necropsia'] = informe.protocolo_necropsia
                context['acta_inspeccion_cadaver'] = informe.acta_inspeccion_cadaver
                context['motivo_peritacion'] = informe.motivo_peritacion
                context['concepto_solicitado'] = informe.concepto_solicitado
                context['resumen_hechos'] = informe.resumen_hechos
                context['ejemplos_estudio'] = informe.ejemplos_estudio
                context['tecnica_empleada'] = informe.tecnica_empleada
                context['examen_exterior_boca'] = informe.examen_exterior_boca
                context['examen_exterior_menton'] = informe.examen_exterior_menton
                context['examen_exterior_peribucal'] = informe.examen_exterior_peribucal
                context['examen_interior_mucosa'] = informe.examen_interior_mucosa
                context['examen_interior_mucogivinal'] = informe.examen_interior_mucogivinal
                context['examen_interior_frenillos'] = informe.examen_interior_frenillos
                context['examen_interior_pisoboca'] = informe.examen_interior_pisoboca
                context['examen_interior_paladarduro'] = informe.examen_interior_paladarduro
                context['examen_interior_paladarblando'] = informe.examen_interior_paladarblando
                context['zona_retromolar'] = informe.zona_retromolar
                context['examen_tejidos_periodontales'] = informe.examen_tejidos_periodontales
                context['examen_tejidos_duros_maxilasuperior_forma'] = informe.examen_tejidos_duros_maxilasuperior_forma
                context['examen_tejidos_duros_maxilasuperior_tamano'] = informe.examen_tejidos_duros_maxilasuperior_tamano
                context['examen_tejidos_duros_maxilasuperior_hallazgos'] = informe.examen_tejidos_duros_maxilasuperior_hallazgos
                context['examen_tejidos_duros_maxilainferior_forma'] = informe.examen_tejidos_duros_maxilainferior_forma
                context['examen_tejidos_duros_maxilainferior_tamano'] = informe.examen_tejidos_duros_maxilainferior_tamano
                context['examen_tejidos_duros_maxilainferior_hallazgos'] = informe.examen_tejidos_duros_maxilainferior_hallazgos
                context['examen_tejidos_duros_maxilainferior_alveolares'] = informe.examen_tejidos_duros_maxilainferior_alveolares
                context['perfil_concavo'] = informe.perfil_concavo
                context['perfil_recto'] = informe.perfil_recto
                context['perfil_convexo'] = informe.perfil_convexo
                context['senales_particulares_odontologicas'] = informe.senales_particulares_odontologicas
                context['valoracion_edad'] = informe.valoracion_edad
                context['observaciones'] = informe.observaciones
                context['examenes_solicitados'] = informe.examenes_solicitados
                context['analisis_conclusiones'] = informe.analisis_conclusiones
                context['nombre_perito'] = informe.nombre_perito
                context['profesion_perito'] = informe.profesion_perito
            except InformeForense.DoesNotExist:
                pass

        if not solo_consultar:
            return render(request,'odontologia/index.html',context)
        else:
            return q,context
    else:
        return redirect('/usuario')

def consultar_forense(request,solo_consultar=False):
    data = {}
    context = armar_contexto_base(request.user)
    if request.user.is_authenticated and context['tipo_perfil'] != "Odontologo":
        ids_pacientes=set()
        dientes = Dientes.objects.all()
        for diente in dientes:
            if str(diente.numero_diente) in request.POST and request.POST[str(diente.numero_diente)] != "":
                data[diente.numero_diente] = request.POST[str(diente.numero_diente)]
                diagnosticos = request.POST[str(diente.numero_diente)].split(",")
                for diagnostico in diagnosticos:
                    comparacion = (len(ids_pacientes)>0)
                    tmp = set()
                    pacientes = PacientesDientes.objects.filter(id_diente=Dientes.objects.get(numero_diente=diente.numero_diente),diagnostico=Codificaciones.objects.get(acronimo=diagnostico))
                    for p in pacientes:
                        if not comparacion:
                            ids_pacientes.add(p.id_paciente.id_paciente)
                            tmp.add(p.id_paciente.id_paciente)
                        else:
                            tmp.add(p.id_paciente.id_paciente)

                    ids_pacientes = set([i for i in ids_pacientes if i in tmp])
        
        pacientes = Pacientes.objects.filter(pk__in=ids_pacientes)
        if len(pacientes) > 0:
            context['sugerencias'] = pacientes


        context['data'] = data
        if solo_consultar:
            return context
        else:
            return render(request,'odontologia/index.html',context)
    else:
        return redirect('/usuario')

def rellenarInforme(request):
    context = armar_contexto_base(request.user)
    context["tipo_perfil"] = request.GET["tipo_perfil"]
    try:
        paciente = Pacientes.objects.get(n_documento=request.GET["n_documento"])
        context['sugerencias'] = [paciente]
        data = {}
        data_raw = PacientesDientes.objects.all().filter(id_paciente=paciente)
        if data_raw != None:
            for dato in data_raw:
                if dato.id_diente.numero_diente not in data:
                    data[dato.id_diente.numero_diente] = dato.diagnostico.acronimo
                else:
                    data[dato.id_diente.numero_diente] += "," + dato.diagnostico.acronimo

        context['data'] = data
        informe = InformeForense.objects.get(paciente=paciente)
        context['numero_informe_pericial'] = informe.numero_informe_pericial
        context['ciudad'] = informe.ciudad
        context['fecha_hora'] = informe.fecha_hora
        context['sexo'] = informe.sexo
        context['autoridad_solicitante'] = informe.autoridad_solicitante
        context['protocolo_necropsia'] = informe.protocolo_necropsia
        context['acta_inspeccion_cadaver'] = informe.acta_inspeccion_cadaver
        context['motivo_peritacion'] = informe.motivo_peritacion
        context['concepto_solicitado'] = informe.concepto_solicitado
        context['resumen_hechos'] = informe.resumen_hechos
        context['ejemplos_estudio'] = informe.ejemplos_estudio
        context['tecnica_empleada'] = informe.tecnica_empleada
        context['examen_exterior_boca'] = informe.examen_exterior_boca
        context['examen_exterior_menton'] = informe.examen_exterior_menton
        context['examen_exterior_peribucal'] = informe.examen_exterior_peribucal
        context['examen_interior_mucosa'] = informe.examen_interior_mucosa
        context['examen_interior_mucogivinal'] = informe.examen_interior_mucogivinal
        context['examen_interior_frenillos'] = informe.examen_interior_frenillos
        context['examen_interior_pisoboca'] = informe.examen_interior_pisoboca
        context['examen_interior_paladarduro'] = informe.examen_interior_paladarduro
        context['examen_interior_paladarblando'] = informe.examen_interior_paladarblando
        context['zona_retromolar'] = informe.zona_retromolar
        context['examen_tejidos_periodontales'] = informe.examen_tejidos_periodontales
        context['examen_tejidos_duros_maxilasuperior_forma'] = informe.examen_tejidos_duros_maxilasuperior_forma
        context['examen_tejidos_duros_maxilasuperior_tamano'] = informe.examen_tejidos_duros_maxilasuperior_tamano
        context['examen_tejidos_duros_maxilasuperior_hallazgos'] = informe.examen_tejidos_duros_maxilasuperior_hallazgos
        context['examen_tejidos_duros_maxilainferior_forma'] = informe.examen_tejidos_duros_maxilainferior_forma
        context['examen_tejidos_duros_maxilainferior_tamano'] = informe.examen_tejidos_duros_maxilainferior_tamano
        context['examen_tejidos_duros_maxilainferior_hallazgos'] = informe.examen_tejidos_duros_maxilainferior_hallazgos
        context['examen_tejidos_duros_maxilainferior_alveolares'] = informe.examen_tejidos_duros_maxilainferior_alveolares
        context['perfil_concavo'] = informe.perfil_concavo
        context['perfil_recto'] = informe.perfil_recto
        context['perfil_convexo'] = informe.perfil_convexo
        context['senales_particulares_odontologicas'] = informe.senales_particulares_odontologicas
        context['valoracion_edad'] = informe.valoracion_edad
        context['observaciones'] = informe.observaciones
        context['examenes_solicitados'] = informe.examenes_solicitados
        context['analisis_conclusiones'] = informe.analisis_conclusiones
        context['nombre_perito'] = informe.nombre_perito
        context['profesion_perito'] = informe.profesion_perito

    except InformeForense.DoesNotExist:
        pass

    return render(request,'odontologia/index.html',context)
    

@register.filter
def get_value(dictionary, key):
    return dictionary.get(key)