from django.db import models

from products.models import Product
from users.models import Client

# Create your models here.


class Order(models.Model):
    """"Clase que representa una Orden de Pedido"""

    date = models.DateTimeField(auto_now_add=True, help_text='fecha')
    status = models.BooleanField(default=True, help_text='estado')
    estimated_time = models.TimeField(help_text='tiempo estimado')
    location = models.CharField(max_length=45, help_text='ubicación')

    # Relaciones
    client = models.ForeignKey(
        Client,
        related_name='orders',
        on_delete=models.CASCADE,
        help_text='cliente'
    )
    products = models.ManyToManyField(
        Product,
        through='Detail',
        blank=True,
        help_text='productos'
    )

    def __str__(self) -> str:
        """
        Función que representa al objeto
        cuando es recuperado

        Retorna:
            String: representa al objeto
        """
        return self.date.strftime('%a %H:%M  %d/%m/%y')


class Detail(models.Model):
    """Clase que representa un Detalle"""

    quantity = models.PositiveIntegerField(help_text='cantidad')

    # Relaciones
    product = models.ForeignKey(
        Product,
        related_name='details',
        on_delete=models.CASCADE,
        help_text='producto'
    )
    order = models.ForeignKey(
        'Order',
        related_name='details',
        on_delete=models.CASCADE,
        help_text='order de pedido'
    )

    def __str__(self) -> str:
        """
        Función que representa al objeto
        cuando es recuperado

        Retorna:
            String: representa al objeto
        """
        return str(self.quantity)
