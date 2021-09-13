from django.db import models
import re

# Create your models here.
class UserManager(models.Manager):
    def validador_basico(self, postData):
        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        SOLO_LETRAS = re.compile(r'^[a-zA-Z. ]+$')

        errors = {}

        if len(postData['name']) < 2:
            errors['name_len'] = "Nombre debe tener al menos 2 caracteres de largo"
        
        if len(postData['lastname']) < 2:
            errors['lastname_len'] = "Apellido debe tener al menos 2 caracteres de largo"

        if not EMAIL_REGEX.match(postData['email']):
            errors['email'] = "Correo invalido"

        if not SOLO_LETRAS.match(postData['name']):
            errors['solo_letras'] = "Solo letras en nombre por favor"

        if len(postData['password']) < 4:
            errors['password'] = "Contraseña debe tener al menos 8 caracteres"

        if postData['password'] != postData['password_confirm'] :
            errors['password_confirm'] = "Contraseña y confirmar contraseña no son iguales. "

        
        return errors

    def validador_citas(self, postData):
        errors = {}
        if len(postData['autor']) < 3:
            errors['autor_len'] = "Autor debe tener al menos 3 caracteres de largo"
        
        if len(postData['mensaje']) < 10:
            errors['mensaje_len'] = "Cita debe tener al menos 10 caracteres de largo"

        return errors
        
class User(models.Model):
    CHOICES = (
        ("user", 'User'),
        ("admin", 'Admin')
    )
    name = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    email = models.EmailField(max_length=255, unique=True)
    role = models.CharField(max_length=255, choices=CHOICES)
    password = models.CharField(max_length=70)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = UserManager()

    def __str__(self):
        return f"{self.name}"

    def __repr__(self):
        return f"{self.name}"

class Quote(models.Model):
    usuario = models.ForeignKey(User, related_name="usuario_quote", on_delete=models.CASCADE)
    autor = models.CharField(max_length=100)
    mensaje = models.CharField(max_length=250)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)