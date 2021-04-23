from django.db import models

from orders.models import Order
from .choices import REVIEW_CHOICES

# Create your models here.


class Review(models.Model):
    """Clase que representa una Valoración"""

    quality_service = models.CharField(max_length=7, choices=REVIEW_CHOICES, help_text='calidad del servicio')
    presentation = models.CharField(max_length=7, choices=REVIEW_CHOICES, help_text='presentación')
    preparation = models.CharField(max_length=7, choices=REVIEW_CHOICES, help_text='preparación')
    ingredients = models.CharField(max_length=7, choices=REVIEW_CHOICES, help_text='ingredientes')
    price = models.CharField(max_length=7, choices=REVIEW_CHOICES, help_text='precio')
    textures = models.CharField(max_length=7, choices=REVIEW_CHOICES, help_text='texturas')
    cooking_point = models.CharField(max_length=7, choices=REVIEW_CHOICES, help_text='punto de cocción')
    comments = models.TextField(help_text='comentarios')
    date = models.DateTimeField(auto_now_add=True)

    # Relaciones
    order = models.OneToOneField(
        Order,
        related_name='review',
        on_delete=models.CASCADE
    )

    def __str__(self) -> str:
        """
        Función que representa al objeto
        cuando es recuperado

        Retorna:
            String: representa al objeto
        """
        return self.quality_service
