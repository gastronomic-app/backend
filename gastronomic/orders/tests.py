from django.test import TestCase
from django.db.utils import IntegrityError

from .models import Order
from .models import Detail
from users.models import Client
from products.models import Product
from enterprises.models import Enterprise

# Create your tests here.


class OrderTest(TestCase):
    # Clase que prueba los attrs del modelo

    def setUp(self) -> None:

        enterprise = Enterprise.objects.create(
            name="Unicauca",
            location='Popayan',
        )

        client = Client.objects.create(
            email="example@gmail.com",
            password="123"
        )

        product = Product.objects.create(
            name="Producto 1",
            price=4500,
            ingredients="Sal, tomate, ajo",
            preparation="Describa aqui",
            estimated_time=4,

            enterprise_id=enterprise.pk,
        )

        order = Order.objects.create(
            estimated_time="4",
            location="Ciudad prueba",

            # Relaciones
            client_id=client.pk
        )

    def test_quantity_negative(self) -> None: #funcion para validar que no se ingrese un valor negativo
        whit self.assertRaises(IntegrityError):
            Detail.objects.create(
                quantity=-40,

                # Relaciones
                order_id=order.pk,
                product_id=product.pk
            )

    def test_status(self) -> None:
        detail = Detail.objects.get(quantity=40)
        self.assertEquals(detail.quantity, 40)
