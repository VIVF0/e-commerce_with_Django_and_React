from django.db import models
from djongo.models import ObjectIdField

class User(models.Model):
    _id = ObjectIdField(primary_key=True)
    user_name = models.CharField(max_length=200)
    email = models.EmailField(unique=True)
    
class Pessoa(models.Model):
    nome = models.CharField(max_length=255)
    email = models.EmailField()

    def __str__(self):
        return self.nome

