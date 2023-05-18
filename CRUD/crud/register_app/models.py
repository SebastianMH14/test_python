from django.db import models

class Registro(models.Model):
    documento = models.IntegerField()
    telefono = models.IntegerField()
    celular = models.IntegerField()
    texto1 = models.TextField()
    texto2 = models.TextField()
    fecha = models.DateField()