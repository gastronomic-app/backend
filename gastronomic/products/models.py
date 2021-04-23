from django.db import models

from enterprises.models import Enterprise
from .choices import PRODUCT_CHOICES

# Create your models here.


class Product(models.Model):
    """Clase que representa un Producto"""

    product_type = models.CharField(max_length=45, choices=PRODUCT_CHOICES, help_text='tipo de producto')
    name = models.CharField(max_length=45, help_text='nombre')
    price = models.PositiveBigIntegerField(help_text='precio')
    ingredients = models.TextField(help_text='ingredientes')
    preparation = models.TextField(null=True, blank=True, help_text='preparación')
    estimated_time = models.PositiveSmallIntegerField(help_text='tiempo estimado')

    # Relaciones
    enterprise = models.ForeignKey(
        Enterprise,
        related_name='products',
        on_delete=models.CASCADE,
        help_text='empresa'
    )
    accompaniments = models.ManyToManyField(
        'self',
        blank=True,
        related_name='products',
        help_text='acompañamientos'
    )

    def __str__(self) -> str:
        """
        Función que representa al objeto
        cuando es recuperado

        Retorna:
            String: representa al objeto
        """
        return self.name


class Image(models.Model):
    """Clase que representa una Imagen"""

    url = models.ImageField(upload_to='uploads/images')

    # Relaciones
    product = models.ForeignKey(
        'Product',
        related_name='images',
        on_delete=models.CASCADE,
        help_text='producto'
    )

    def __str__(self) -> str:
        """
        Función que representa al objeto
        cuando es recuperado

        Retorna:
            String: representa al objeto
        """
        return self.url.name
