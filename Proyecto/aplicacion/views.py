from django.shortcuts import render,HttpResponse,redirect
from django.db import IntegrityError
from .models import Cliente
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
# Create your views here.

def home(request):
    return render(request, 'index.html')


def mujer(request):
    return render(request, 'Mujer.html')

def oversize(request):
    return render(request,'Oversize.html')

def hombre(request):
    return render(request,'Hombre.html')

def infantil(request):
    return render(request,'Infantil.html')


def registro(request):
    if request.method == 'GET':

        return render(request,'registro.html')
    else:                
        #print("metodo post ")
        rut = request.POST.get('rut')
        nombres = request.POST.get('nombre')
        apellidos = request.POST.get('apellidos')
        email = request.POST.get('correo')
        direccion =request.POST.get('direccion')
        print(rut,nombres,apellidos,email,direccion)

        try:
            cliente = Cliente.objects.create(
                rut=rut,
                nombres=nombres,
                apellidos=apellidos,
                email=email,
                direccion=direccion,
                activo=True
            )
            return render(request, 'index.html')
        except IntegrityError:
            # El correo electrónico ya existe en la base de datos
            error_message = "El correo electrónico ya existe en la base de datos. Por favor, ingresa un correo electrónico diferente."
            return render(request, 'registro.html', {'error_message': error_message})
        
@login_required
def crud(request):
    usuarios = Cliente.objects.all()
    context ={'usuarios': usuarios}
    return render(request,'registro/lista.html',context)

@login_required    
def del_usuarios(request,pk):
    context={}
    try:
        usuario=Cliente.objects.get(rut=pk)
        usuario.delete()
        mensaje="USUARIO ELIMINADO"
        usuarios = Cliente.objects.all()
        context={'usuarios': usuario,'mensaje':mensaje }
        return render(request,'registro/lista.html',context)
    except:
        mensaje='RUT NO EXISTE'
        usuario = Cliente.objects.all()
        context = {'usuarios':usuario, 'mensaje':mensaje}
        return render(request,'registro/lista.html',context) 
@login_required   
def mod_usuarios(request,pk):
    if pk != "":
        usuario=Cliente.objects.get(rut=pk)
        
        context={'usuario':usuario}
        if usuario:
            return render(request,'registro/edicion_usuario.html',context)
        else:
            context={'mensaje':'RUT NO ENCONTRADO'}
            return render(request,'registro/lista.html',context)
        
        
@login_required       
def insertar_usuario(request):
    if request.method=="POST":
        rut=request.POST["rut"]
        nombre=request.POST["nombre"]
        
        usuario = Cliente()
        usuario.rut=rut
        usuario.nombre=nombre
        usuario.save()
        
        context={'DATOS ACTUALIZADO DEL USUARIO':usuario}
        return render(request, 'registro/edicion_usuario.html',context)
    else:
        usuarios = Cliente.objects.all()
        context={'usuarios':usuarios}
        return render(request, 'registro/lista.html',context)
    
def iniciar_sesion(request):
    return render(request,'registration\login.html')
