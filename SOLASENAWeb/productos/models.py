from django.db import models

# Create your models here.

class producto(models.Model):
    titulo=models.CharField(max_length=50)
    contenido=models.CharField(max_length=60)
    imagen=models.ImageField(upload_to='productos')
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now_add=True)
    
    class meta:
        verbose_name='servicio'
        verbose_name_plural='servicios'

    def __str__(self):
        return self.titulo
