from django.shortcuts import render
from crud.models import Usuario, User, Eps, Rol
from crud.forms import  UsuarioForm, UserForm, SignUpForm, EpsForm, RolForm
import json
from django.http import HttpResponse
from django import forms
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.http import HttpResponse

# Create your views here.
from django.contrib.auth.decorators import login_required
@login_required
def allUsers(request):
    """
    View for show all users
    """
    users = Usuario.objects.all()
    context = {
        'users': users
    }
    return render(request, 'index.html', context)

@login_required
def createUser(request):
    """
    docstring
    """
    # POST method is used to add or create new User in this view
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        signUpFormInstance = SignUpForm(request.POST)
        usuarioFormInstance = UsuarioForm(request.POST)
        epsFormInstance = EpsForm(request.POST)
        rolFormInstance = RolForm(request.POST)
        # check whether it's valid:
        if signUpFormInstance.is_valid() and usuarioFormInstance.is_valid() and epsFormInstance.is_valid() and rolFormInstance.is_valid():
            eps = epsFormInstance.cleaned_data['eps_name']
            rol = rolFormInstance.cleaned_data['rol_name']
            try:
                eps_instance = Eps.objects.get(eps_name=eps)
                rol_instance = Rol.objects.get(rol_name=rol)
            except:
                eps_instance = Eps.objects.create(eps_name=eps)
                rol_instance = Rol.objects.create(rol_name=rol)
            usuario = usuarioFormInstance.save()
            usuario.rol = rol_instance
            usuario.eps = eps_instance
            usuario.user = signUpFormInstance.save()
            usuario.save()
            return HttpResponseRedirect(reverse_lazy('list'))
        else:
            context = { 'usuarioForm': usuarioFormInstance, 'userForm': signUpFormInstance, 'epsForm': epsFormInstance, 'rolForm': rolFormInstance }
            return render(request, 'create.html', context)

    context = {
        'usuarioForm': UsuarioForm,
        'userForm': SignUpForm,
        'epsForm': EpsForm,
        'rolForm': RolForm
    }
    return render(request, 'create.html', context)

@login_required
def updateUser(request, user_id):
    """
    docstring
    """
    print("the userid is:  ", user_id)
    user_to_update = User.objects.get(id=user_id)
    usuario = Usuario.objects.get(user=user_to_update)
    # POST method is used to add or create new User in this view
    if request.method == 'POST':
        usuarioForm = UsuarioForm(request.POST, instance=usuario)
        userForm = UserForm(request.POST, instance=user_to_update)
        if usuarioForm.is_valid() and userForm.is_valid():
            usuarioForm.save()
            userForm.save()
            messages.success(request, 'User is updated successfully!')
            return HttpResponseRedirect(reverse_lazy('list'))
        else:
            messages.error(request, 'Ups! No updated successfully!')
            return HttpResponseRedirect(reverse_lazy('list'))
    else:
        usuarioForm = UsuarioForm(instance=usuario)
        userForm = UserForm(instance=user_to_update)

    context = {
        'usuarioForm': usuarioForm,
        'userForm':userForm,
        'user_id': user_id
    }
    return render(request, 'update.html', context)

@login_required
def deleteUser(request):
    """
    docstring
    """
    if request.method == "POST":
        data = json.loads(request.body)
        print("*********", data)
        User.objects.get(pk=data['userId']).delete()

    return Httpresponse("Done!")