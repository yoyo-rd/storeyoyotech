"""
from django.db import models

class Producto(models.Model):
    CODIGO_TIPO = (
        ('local', 'Local'),
        ('internacional', 'Internacional'),
    )
    
    codigo = models.CharField(max_length=50, unique=True)
    descripcion = models.TextField()
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    tipo = models.CharField(max_length=13, choices=CODIGO_TIPO)
    imagen_url = models.URLField(max_length=200, blank=True)  # Enlace de la imagen

    def __str__(self):/fg
        return self.descripcion
"""

from django.db import models


class Producto(models.Model):
    codigo = models.CharField(max_length=100)
    descripcion = models.TextField()
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    tipo = models.CharField(max_length=20, choices=[('local', 'Local'), ('internacional', 'Internacional')])
    imagen = models.ImageField(upload_to='productos/', null=True, blank=True)

    def __str__(self):
        return self.descripcion
