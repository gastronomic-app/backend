from django.db import models

from .choices import PAYMENT_TYPE_CHOICES

# Create your models here.


class Payment(models.Model):
    """Clase que representa un Pago"""

    payment_type = models.CharField(max_length=11, choices=PAYMENT_TYPE_CHOICES, help_text='tipo pago')
    payment_value = models.PositiveBigIntegerField(help_text='valor pago')

    def __str__(self) -> str:
        """
        Función que representa al objeto
        cuando es recuperado

        Retorna:
            String: representa al objeto
        """
        return self.payment_type
