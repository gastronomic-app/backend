from django.db.models import (
    Model,
    CharField,
    PositiveBigIntegerField,
    OneToOneField,
    CASCADE
)

from orders.models import Order
from .choices import PAYMENT_TYPE_CHOICES

# Create your models here.


class Payment(Model):
    """Clase que representa un Pago"""

    payment_type = CharField(max_length=18, choices=PAYMENT_TYPE_CHOICES, help_text='tipo pago')
    payment_value = PositiveBigIntegerField(help_text='valor pago')

    # Relaciones
    order = OneToOneField(
        Order,
        related_name='payment',
        on_delete=CASCADE,
        help_text='orden pedido'
    )

    def __str__(self) -> str:
        """
        Función que representa al objeto
        cuando es recuperado
        """

        return self.payment_type
