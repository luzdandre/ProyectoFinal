from sqlite3 import Cursor
from django.shortcuts import render, HttpResponse
from django.http import HttpResponse
from Home.models import Gerencia, Areas, Empleados, Vacaciones, Avatar

from Home.forms import AreasFormulario, EmpleadosFormulario, GerenciasFormulario, VacacionesFormulario, UserRegisterForm, UserEditForm

from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required


#from django.db.models import Q

# Create your views here.
#@login_required
def inicio(request):
    #avatares= Avatar.objects.filter(user= request.user.id)

    return render(request, "Home/inicio.html")
    #, {"url":avatares[0].imagen.url})

def areas(request):

    return render(request, "Home/areas.html")


def empleados(request):

    return render(request, "Home/empleados.html")

def gerencia(request):

    return render(request,"Home/gerencia.html")

def vacaciones(request):

    return render(request,"Home/vacaciones.html")

def about(request):

    return render(request,"Home/about.html")

def prox(request):

    return render(request,"Home/prox.html")



def areas(request):
    if request.method == 'POST':
        miFormulario= AreasFormulario(request.POST)
        print(miFormulario)

        if miFormulario.is_valid:

            informacion= miFormulario.cleaned_data

            areas= Areas(nombre_sector=informacion['nombre_sector'],cant_empleados=informacion['cant_empleados'],puestos_vacantes=informacion['puestos_vacantes'])

            areas.save()
            return render(request,"Home/inicio.html",{"mensaje": f"Area ingresada"})
    
    else:

        miFormulario= AreasFormulario()

    return render(request,"Home/areas.html",{"miFormulario":miFormulario})


def empleados(request):
    if request.method == 'POST':
        miFormulario= EmpleadosFormulario(request.POST)
        print(miFormulario)

        if miFormulario.is_valid:

            informacion= miFormulario.cleaned_data

            empleados= Empleados(nombre=informacion['nombre'],apellido=informacion['apellido'],area=informacion['area'],fecha_ingreso=informacion['fecha_ingreso'])

            empleados.save()
            return render(request,"Home/inicio.html",{"mensaje": f"Empleado registrado"})
    
    else:

        miFormulario= EmpleadosFormulario()

    return render(request,"Home/empleados.html",{"miFormulario":miFormulario})  


def gerencia(request):
    if request.method == 'POST':
        miFormulario= GerenciasFormulario(request.POST)
        print(miFormulario)

        if miFormulario.is_valid:

            informacion= miFormulario.cleaned_data

            gerencia= Gerencia(nombre_gerencia=informacion['nombre_gerencia'],director=informacion['director'],cant_empleados=informacion['cant_empleados'])

            gerencia.save()
            return render(request,"Home/inicio.html",{"mensaje": f"Gerencia registrada"})
    
    else:

        miFormulario= GerenciasFormulario()

    return render(request,"Home/gerencia.html",{"miFormulario":miFormulario})


def vacaciones(request):
    if request.method == 'POST':
        miFormulario= VacacionesFormulario(request.POST)
        print(miFormulario)

        if miFormulario.is_valid:

            informacion= miFormulario.cleaned_data

            vacaciones= Vacaciones(fecha_solicitud=informacion['fecha_solicitud'],solicitante=informacion['solicitante'],inicio_vacaciones=informacion['inicio_vacaciones'],fin_vacaciones=informacion['fin_vacaciones'])

            vacaciones.save()
            return render(request,"Home/inicio.html",{"mensaje": f"Vacaciones solicitadas"})
    
    else:

        miFormulario= VacacionesFormulario()

    return render(request,"Home/vacaciones.html",{"miFormulario":miFormulario})

def buscar(request):
    if request.GET["director"]:
        director= request.GET['director']
        print(director)

        gerencia = Gerencia.objects.filter(director__icontains=director)
        print(gerencia)

        return render(request,"Home/buscar_gerencia.html", {"gerencia":gerencia,"director":director})
    
    else:
        respuesta = "No enviaste datos"

    return render(request,"Home/buscar_gerencia.html", {"respuesta":respuesta})


def leerGerencia(request):

      gerencia = Gerencia.objects.all() 

      contexto= {"gerencia":gerencia} 

      return render(request, "Home/leerGerencia.html",contexto)


def eliminarGerencia(request, nombre_gerencia):

      gerencia = Gerencia.objects.get(nombre_gerencia=nombre_gerencia)
      gerencia.delete()
      
      #vuelvo al menú
      gerencia = Gerencia.objects.all() #trae todos los profesores

      contexto= {"gerencia":gerencia} 

      return render(request, "Home/leerGerencia.html",contexto)  


def editarGerencia(request, nombre_gerencia):

      #Recibe el nombre del profesor que vamos a modificar
      gerencia = Gerencia.objects.get(nombre_gerencia=nombre_gerencia)

      #Si es metodo POST hago lo mismo que el agregar
      if request.method == 'POST':

            miFormulario = GerenciasFormulario(request.POST) #aquí mellega toda la información del html

            print(miFormulario)

            if miFormulario.is_valid:   #Si pasó la validación de Django

                  informacion = miFormulario.cleaned_data

                  gerencia.nombre_gerencia = informacion['nombre_gerencia']
                  gerencia.director = informacion['director']
                  gerencia.cant_empleados = informacion['cant_empleados']


                  gerencia.save()

                  return render(request, "Home/inicio.html") #Vuelvo al inicio o a donde quieran
      #En caso que no sea post
      else: 
            #Creo el formulario con los datos que voy a modificar
            miFormulario= GerenciasFormulario(initial={'nombre_gerencia': gerencia.nombre_gerencia, 'director':gerencia.director , 
            'cant_empleados':gerencia.cant_empleados}) 

      #Voy al html que me permite editar
      return render(request, "Home/editarGerencia.html", {"miFormulario":miFormulario, "nombre_gerencia":nombre_gerencia})


class EmpleadosList(ListView):
    model= Empleados
    template_name= "Home/empleados_list.html"

class EmpleadosDetalle(DetailView):
    model= Empleados
    template_name="Home/empleados_detalle.html"

class EmpleadosCreacion(CreateView):

      model = Empleados
      success_url = "/Home/empleados_list"
      fields = ['nombre', 'apellido','area','fecha_ingreso']


class EmpleadosUpdate(UpdateView):

      model = Empleados
      success_url = "/Home/empleados_list"
      fields  = ['nombre', 'apellido','area','fecha_ingreso']


class EmpleadosDelete(DeleteView):

      model = Empleados
      success_url = "/Home/empleados_list"




def login_request(request):
      
      if request.method == "POST":
           
            form = AuthenticationForm(request, data = request.POST)
            
            if form.is_valid():
                  usuario = form.cleaned_data.get('username')
                  contra = form.cleaned_data.get('password')
               
                  user = authenticate(username = usuario , password = contra)
                 
                  if user is not None:
                        login(request, user)

                        return render (request, "Home/inicio.html", {"mensaje": f"Bienvenido/a {usuario}"})
                  else:
                       
                        return render (request, "Home/inicio.html", {"mensaje":"Error en los datos"})
            else:
                  return render(request, "Home/inicio.html", {"mensaje":"Formulario erroneo"})
      
      
      form = AuthenticationForm()
    
      return render(request, "Home/login.html", {'form': form})



def register(request):

      
    if request.method == "POST":

        form = UserCreationForm(request.POST)
            
        if form.is_valid():
            
            username = form.cleaned_data['username']
            form.save()
            return render(request, "Home/inicio.html", {"mensaje": "usuario creado"})

    else: 
        form = UserRegisterForm()

    return render(request, "Home/registro.html", {"form": form})

@login_required
def editarPerfil(request):
      
      usuario = request.user
      
      if request.method == 'POST':
            miFormulario = UserEditForm(request.POST)
            if miFormulario.is_valid(): 
                  informacion = miFormulario.cleaned_data
                  
                 
                  usuario.email = informacion['email']
                  usuario.password1 = informacion['password1']
                  usuario.password2 = informacion['password2']
                  usuario.save()
            
                  return render(request, "Home/inicio.html",{"mensaje": "usuario modificado"}) 

      else:
            
            miFormulario = UserEditForm(initial={'email':usuario.email})
      
      
      return render(request, "Home/editarPerfil.html", {"miFormulario": miFormulario, "usuario": usuario})



     
    
    