from django.contrib import admin

from crud.models import Usuario, Rol, Eps
# Register your models here.
admin.site.register(Usuario)
admin.site.register(Rol)
admin.site.register(Eps)