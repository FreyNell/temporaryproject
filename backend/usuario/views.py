from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login, logout
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from odontologia.models import Perfiles, TipoPerfil

class SignUpForm(UserCreationForm):
    GEEKS_CHOICES =(
        ("Odontologo", "Odontologo"),
        ("Investigador", "Investigador"),
    )
    username = forms.CharField(label="Usuario",max_length=30,widget=forms.TextInput(attrs={'class': 'form-control'}))
    password1 = forms.CharField(label="Contraseña",max_length=30,widget=forms.PasswordInput(attrs={'class': 'form-control','type':'password'}))
    password2 = forms.CharField(label="Confirmar Contraseña",max_length=30,widget=forms.PasswordInput(attrs={'class': 'form-control','type':'password'}))
    tipo_perfil = forms.ChoiceField(choices = GEEKS_CHOICES,widget=forms.Select(attrs={'class':'form-select'}))

    class Meta:
        model = User
        fields = ('username', 'password1', 'password2', )

def login_view(request):
    if not request.user.is_authenticated:
        if "usuario" in request.POST:
            user = authenticate(username=request.POST['usuario'], password=request.POST['contrasena'])
            if user is not None:
                login(request, user)
                return redirect('/')
            else:
                context = { 'error_message' : "Usuario o Contraseña incorrecto."}
                return render(request,'usuario/login.html',context)
    
        return render(request,'usuario/login.html')
    else:
        return redirect('/')

def logout_view(request):
    logout(request)
    return redirect('/')

def registrar(request):
    if not request.user.is_authenticated:
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            perfil = Perfiles()
            perfil.usuario = User.objects.get(username=username)
            perfil.tipo_perfil = TipoPerfil.objects.get(nombre_perfil=form.cleaned_data.get('tipo_perfil'))
            perfil.save()
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('/')
        else:
            form = SignUpForm()
        return render(request, 'usuario/registrar.html',{'form': form})
    else:
        return redirect('/')