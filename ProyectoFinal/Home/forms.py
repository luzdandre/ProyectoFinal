from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class AreasFormulario(forms.Form):

    nombre_sector= forms.CharField()
    cant_empleados= forms.IntegerField()
    puestos_vacantes= forms.IntegerField()

class EmpleadosFormulario(forms.Form):

    nombre= forms.CharField()
    apellido= forms.CharField()
    area= forms.CharField()
    fecha_ingreso=forms.DateField()

class GerenciasFormulario(forms.Form):

    nombre_gerencia= forms.CharField()
    director= forms.CharField()
    cant_empleados= forms.IntegerField()

class VacacionesFormulario(forms.Form):
    fecha_solicitud= forms.DateField()
    solicitante= forms.CharField()
    inicio_vacaciones= forms.DateField()
    fin_vacaciones= forms.DateField()

class UserRegisterForm(UserCreationForm):
    
    email= forms.EmailField()
    password1 = forms.CharField(label= 'Contraseña', widget= forms.PasswordInput)
    password2 = forms.CharField(label= 'repite la contraseña', widget=forms.PasswordInput)
   
    class Meta:
        model = User
        print(model)
        fields = ['username','email','password1', 'password2']

        help_texts= {k:"" for k in fields}

class UserEditForm(UserCreationForm): 
   
    
    email = forms.EmailField(label='modificar email')
    password1 = forms.CharField(label='contraseña', widget=forms.PasswordInput)
    password2 = forms.CharField(label= 'repita contraseña', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['email', 'password1', 'password2']
        help_texts= {k:"" for k in fields}
