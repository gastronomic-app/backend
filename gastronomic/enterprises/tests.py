from django.test import TestCase

from .models import Enterprise

# Create your tests here.


class EnterpriseTest(TestCase):
    def setUp(self) -> None:
        Enterprise.objects.create(
            name='test 1',
            location='avenida siempre viva 742',
        )
    
    def test_status(self):
        """Prueba del estado de la empresa"""
        enterprise = Enterprise.objects.get(name='test 1')
        self.assertEquals(enterprise.status, True)
