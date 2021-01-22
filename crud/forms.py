from .models import Usuario, User, Eps, Rol
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django import forms


class SignUpForm(UserCreationForm):

    username = forms.CharField(widget=forms.EmailInput(
        attrs={'placeholder':'example@mail.com' }
    ))

    class Meta(UserCreationForm.Meta):
        model = User
        fields = [
            'username',
            'password1', 
            'password2', 
        ]


class UserForm(ModelForm):
    class Meta:
        model = User
        fields = [
            'username',
        ]

class UsuarioForm(ModelForm):
    """
    docstring
    """
    class Meta:
        model = Usuario
        fields = [
            'name',
            'card_id',
            'gender',
            'phone',
            'dob',
        ]
        labels = {
            "dob": "Fecha de Nacimiento",
        }

class EpsForm(ModelForm):
    class Meta:
        model = Eps
        fields = [
            'eps_name'
        ]
        labels = {
            "eps_name": "EPS",
        }

class RolForm(ModelForm):
    class Meta:
        model = Rol
        fields = [
            'rol_name'
        ]
        labels = {
            "rol_name": "Rol",
        }