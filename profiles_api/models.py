from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.models import BaseUserManager
from django.conf import settings

class UserProfileManager(BaseUserManager):
    """manager para perfiles de usuario"""

    def create_user(self, email, name, password=None):
        """crear nuevo user profile"""
        if not email:
            raise ValueError('usuario debe de tener un email')
        email =self.normalize_email(email)
        user =self.model(email=email,name=name)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self,email,name,password):
        user = self.create_user(email,name,password)
        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)
        return user  

class UserProfile(AbstractBaseUser,PermissionsMixin):
    """MODELO DE BASE DE DATOS PARA USUARIOS EN EL SISTEMA"""
    email = models.EmailField(max_length=50, unique=True)
    name = models.CharField(max_length=50)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)


    objects = UserProfileManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']

    def get_full_name(self):
        """obtener nombre completo del usuario """
        return self.name


    def get_short_name(self):
        """obtener nombre corto del usuario"""
        return self.name

    def __str__(self):
        """retornar cadena representando nuestro usuario"""
        return self.email    

class ProfileFeedItem(models.Model):
    """perfil de status update"""
    UserProfile = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete= models.CASCADE,
        primary_key=True
    )

    status_text = models.CharField(max_length=100)
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """retornar modelo en cadena"""
        return self.status_text



class SillasProfileManager(BaseUserManager):
    """manager para perfiles de usuario"""
    def create_silla(self, fecha, silla):
        """nueva fecha registrada"""
        if not fecha:
            raise ValueError('debes de polocar una fecha y numero de silla')
        user = self.model(fecha=fecha, silla=silla)
        user.save(using=self._db)
        return user

    def delete(self, id):
        sillas = self.model(id=id)
        sillas.delete(using=self._db)
        return {"status": "Done"}



class SillasProfile(AbstractBaseUser):
    """modelo para usuarios en el sistema"""
    fecha = models.DateField(max_length=50)
    silla = models.CharField(max_length=100, unique=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default= False)

    object = SillasProfileManager()

    USERNAME_FIELD = 'fecha'
    REQUIRED_FIELDS = ['silla']

    def get_full_name(self):
        """obtener nombre completo del usuario """
        return self.silla


    def get_short_name(self):
        """obtener nombre corto del usuario"""
        return self.silla

    def __str__(self):
        """retornar cadena representando nuestro usuario"""
        return str(self.fecha)  

    