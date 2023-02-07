from django.db import models

class estudiantes(models.Model):
    nombre=models.CharField(max_length=15)
    apellido=models.CharField(max_length=15)
    camada=models.IntegerField()
    def __str__(self):
        return f"nombre: {self.nombre}////camada: {self.camada}"

class profesores(models.Model):
    def __str__(self):
        return f"nombre: {self.nombre}////camada: {self.camada}"
    nombre=models.CharField(max_length=15)
    apellido=models.CharField(max_length=15)
    camada=models.IntegerField()

class cursos(models.Model):
    curso=models.CharField(max_length=30)
    camada=models.IntegerField()
    
