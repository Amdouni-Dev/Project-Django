from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.exceptions import ValidationError
from django.core.validators import *
from django.utils.html import format_html
# Create your models here.
def validMail(value):
    if not str(value).endswith("@esprit.tn"):
        raise ValidationError("mail")
    return value

def ValidLength(value):
    if len(value)!=8:
        raise ValidationError("le longueur de num cin doit avoir 8 caracteres")
    return value 
class Person(AbstractUser):
  
    #image = models.ImageField(upload_to='../users/imges/',blank=True)
    
    cin=models.CharField(primary_key=True, max_length=255,validators=[MinLengthValidator(8,message='La valeur doit contenir au moins 8 caracteres '),MaxLengthValidator(8,"La valeur doit avoir au max 8 caracteres ")])
    email=models.EmailField(unique=True)
    username=models.CharField(max_length=10,unique=True)
    USERNAME_FIELD='username'
    # def image_tag(self):
    #     return format_html('<img src="{}" width="50" />'.format(self.image.url))
    # image_tag.short_description = 'Image'
    def __str__(self):
        return self.username
    class Meta:
        #bech nbadel esm l model fel interface 
         verbose_name = "Details de l'utilisateur"
 
        

    
    
# Create your models here.

# class Person(AbstractUser):
#     cin=models.CharField(primary_key=True, max_length=255)
#     email=models.EmailField(unique=True)
#     username=models.CharField(max_length=10,unique=True)
#     USERNAME_FIELD='username'
