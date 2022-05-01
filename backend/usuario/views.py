from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login, logout

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
