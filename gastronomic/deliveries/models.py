from django.db import models

from orders.models import Order
from payments.models import Payment
from users.models import Courier

# Create your models here.


class Delivery(models.Model):
    """Clase que representa una Entrega"""

    status = models.BooleanField(default=False, help_text='estado')
    delivery_time = models.DateTimeField(auto_now_add=True, help_text='hora entrega')

    class Meta:
        verbose_name_plural = 'deliveries'

    # Relaciones
    payment = models.OneToOneField(
        Payment,
        related_name='delivery',
        on_delete=models.CASCADE,
        help_text='pago'
    )
    courier = models.ForeignKey(
        Courier,
        related_name='deliveries',
        on_delete=models.CASCADE,
        help_text='mensajero'
    )
    order = models.OneToOneField(
        Order,
        related_name='delivery',
        on_delete=models.CASCADE,
        help_text='orden de pedido'
    )

    def __str__(self) -> str:
        """
        Función que representa al objeto
        cuando es recuperado

        Retorna:
            String: representa al objeto
        """
        return self.status
