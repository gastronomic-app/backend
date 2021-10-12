from django.db.models import (
    Model,
    DateTimeField,
    PositiveSmallIntegerField,
    CharField,
    ForeignKey,
    ManyToManyField,
    CASCADE
)
from django.core.exceptions import ValidationError
from django.db.models.fields import TextField

from products.models import Product
from users.models import Client, Courier
from .choices import STATUS_CHOICES, NEW

# Create your models here.


class Order(Model):
    """"Clase que representa una Orden de Pedido"""

    date = DateTimeField(auto_now_add=True, help_text='fecha')
    status = CharField(max_length=15, choices=STATUS_CHOICES, default=NEW, help_text='estado')
    estimated_time = CharField(max_length=45, help_text='tiempo estimado')
    location = CharField(max_length=250, help_text='ubicación')
    complaint = TextField(blank=True, null=True, help_text='queja')

    # Relaciones
    client = ForeignKey(
        Client,
        related_name='orders_clients',
        on_delete=CASCADE,
        help_text='cliente'
    )
    products = ManyToManyField(
        Product,
        related_name='orders',
        through='Detail',
        blank=True,
        help_text='productos'
    )
    courier = ForeignKey(
        Courier,
        blank=True,
        null=True,
        related_name='orders_couriers',
        on_delete=CASCADE,
        help_text='mensajero'
    )

    def __str__(self) -> str:
        """
        Función que representa al objeto
        cuando es recuperado
        """

        return self.date.strftime('%a %H:%M  %d/%m/%y')


class Detail(Model):
    """
    Clase que representa el Detalle entre
    Productos y Ordenes de Pedidos
    """

    quantity = PositiveSmallIntegerField(help_text='cantidad')

    # Relaciones
    product = ForeignKey(
        Product,
        related_name='details',
        on_delete=CASCADE,
        help_text='producto'
    )
    order = ForeignKey(
        'Order',
        related_name='details',
        on_delete=CASCADE,
        help_text='orden de pedido'
    )

    def clean(self) -> None:
        if self.quantity == 0:
            raise ValidationError(_('No se puede guardar 0'))
        return super().clean()

    def __str__(self) -> str:
        """
        Función que representa al objeto
        cuando es recuperado
        """

        return str(self.quantity)
