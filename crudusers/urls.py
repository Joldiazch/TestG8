"""crudusers URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from crud import views as CrudViews

urlpatterns = [
    path('', CrudViews.allUsers),
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    path('users/', CrudViews.allUsers, name='list'),
    path('update/<int:user_id>/', CrudViews.updateUser, name='update'),
    path('create/', CrudViews.createUser, name='create'),
    path('delete/', CrudViews.deleteUser, name='delete'),
]
