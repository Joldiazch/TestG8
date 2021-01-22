from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Eps(models.Model):
    """ Model representation of EPS on User Crud """

    eps_name = models.CharField(max_length=20)

    def __str__(self):
        return self.eps_name

    class Meta:
        db_table = ''
        managed = True
        verbose_name = 'Eps'
        verbose_name_plural = 'Epss'

class Rol(models.Model):
    """ Model representation to user rol Exam: Medico, User, ETC.. """

    rol_name = models.CharField(max_length=20)

    def __str__(self):
        return self.rol_name

    class Meta:
        db_table = ''
        managed = True
        verbose_name = 'Rol'
        verbose_name_plural = 'Rols'

class Usuario(models.Model):

    """ Model representation of an general User """
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)

    name = models.CharField(max_length=20)
    card_id = models.CharField(max_length=20)
    gender = models.CharField(max_length=20)
    phone = models.CharField(max_length=15)
    dob = models.DateField()

    eps = models.ForeignKey(Eps, on_delete=models.CASCADE, null=True)
    rol = models.ForeignKey(Rol, on_delete=models.CASCADE, null=True)
    create_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        managed = True
        verbose_name = 'Usuario'
        verbose_name_plural = 'Usuarios'