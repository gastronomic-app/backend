from django.test import TestCase
from django.db.utils import IntegrityError

from .models import Order
from .models import Detail
from users.models import Client
from products.models import Product
from enterprises.models import Enterprise

# Create your tests here.


class DetailTest(TestCase):
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

            enterprise_id=enterprise.id
        )

        order = Order.objects.create(
            estimated_time="4",
            location="Ciudad prueba",

            # Relaciones
            client_id=client.id
        )

# funcion para validar que no se ingrese un valor negativo
    def test_quantity_negative(self) -> None:
        order = Order.objects.first()
        product = Product.objects.first()

        with self.assertRaises(IntegrityError):
            Detail.objects.create(
                quantity=-40,

                # Relaciones
                order_id=order.id,
                product_id=product.id
            )

    def test_quantity(self) -> None:
        order = Order.objects.first()
        product = Product.objects.first()
        detail =  Detail.objects.create(
                quantity=40,

                # Relaciones
                order_id=order.id,
                product_id=product.id
            )
        self.assertEquals(detail.quantity, 40)

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

            enterprise_id=enterprise.id
        )

    def test_negative_estimate_time(self)-> None:
        client = Client.objects.first()
        with self.assertRaises(IntegrityError):
            order = Order.objects.create(
                estimated_time=-4,
                location="Ciudad prueba",

                # Relaciones
                client_id=client.id
            )
