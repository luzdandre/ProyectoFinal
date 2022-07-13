from django.urls import path

from Home import views
from django.contrib.auth.views import LogoutView

urlpatterns= [

    path('',views.inicio,name="Inicio"),
    path('areas',views.areas,name="Areas"),
    path('empleados',views.empleados,name="Empleados"),
    path('gerencia',views.gerencia,name="Gerencia"),
    path('vacaciones',views.vacaciones,name="Vacaciones"),
    path('about',views.about,name="about"),
    path('prox',views.prox, name="prox"),
    path('areasFormulario',views.areas,name="AreasFormulario"),
    path('empleadosFormulario',views.empleados,name="EmpleadosFormulario"),
    path('gerenciasFormulario',views.gerencia,name="GerenciasFormulario"),
    path('vacacionesFormulario',views.vacaciones,name="VacacionesFormulario"),
    path('leerGerencia', views.leerGerencia, name="LeerGerencia"),    
    path('eliminarGerencia/<nombre_gerencia>/', views.eliminarGerencia, name="EliminarGerencia"),
    path('editarGerencia/<nombre_gerencia>/', views.editarGerencia, name="EditarGerencia"),
    path('buscar/',views.buscar),
    path('empleados_list', views.EmpleadosList.as_view(), name='List'),
    path(r'^(?P<pk>\d+)$', views.EmpleadosDetalle.as_view(), name='Detail'),
    path(r'^nuevo$', views.EmpleadosCreacion.as_view(), name='New'),
    path(r'^editar/(?P<pk>\d+)$', views.EmpleadosUpdate.as_view(), name='Edit'),
    path(r'^borrar/(?P<pk>\d+)$', views.EmpleadosDelete.as_view(), name='Delete'),
    path('login',views.login_request, name='Login'),
    path('register', views.register, name= 'Register'),
    path('logout', LogoutView.as_view(template_name='Home/logout.html'), name='logout'),
    path('editarPerfil',views.editarPerfil, name="EditarPerfil"),
   ]