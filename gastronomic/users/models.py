from django.db import models
from django.conf import settings

from .choices import ROLE_CHOICES

# Create your models here.


class User(models.Model):
    """
    Clase abstracta para
    Clientes, Mensajeros y
    Administradores de Establecimientos
    """
    names = models.CharField(max_length=45, help_text='nombres')
    lastnames = models.CharField(max_length=45, help_text='apellidos')
    location = models.CharField(max_length=45, help_text='ubicación')
    telephone = models.CharField(max_length=15, help_text='telefono')
    role = models.PositiveSmallIntegerField(choices=ROLE_CHOICES, help_text='rol en el sistema')
    created = models.DateTimeField(auto_now_add=True, help_text='creado')
    updated = models.DateTimeField(auto_now=True, help_text='actualizado')

    class Meta:
        abstract = True


class EstablishmentManager(User):
    """Clase que representa un Administrador del Establecimiento"""

    # Relaciones
    user_profile = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        help_text='perfil de usuario'
    )
    enterprises = models.ManyToManyField(
        'enterprises.Enterprise',
        through='enterprises.Manager',
        related_name='establishments_managers',
        help_text='empresas'
    )

    def __str__(self) -> str:
        """
        Función que representa al objeto
        cuando es recuperado

        Retorna:
            String: representa al objeto
        """
        return self.names


class Client(User):
    """Clase que representa un Cliente"""

    # Relaciones
    user_profile = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        help_text='perfil de usuario'
    )

    def __str__(self) -> str:
        """
        Función que representa al objeto
        cuando es recuperado

        Retorna:
            String: representa al objeto
        """
        return self.names


class Courier(User):
    """Clase que representa un Mensajero"""

    license_plate = models.CharField(max_length=45, help_text='placa')

    # Relaciones
    enterprise = models.ForeignKey(
        'enterprises.Enterprise',
        related_name='couriers',
        on_delete=models.CASCADE,
        help_text='establecimiento'
    )
    user_profile = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        help_text='perfil de usuario'
    )


    def __str__(self) -> str:
        """
        Función que representa al objeto
        cuando es recuperado

        Retorna:
            String: representa al objeto
        """
        return self.names
