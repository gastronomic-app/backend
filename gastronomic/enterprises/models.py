from django.db.models import (
    Model,
    CharField,
    BooleanField,
    DateTimeField,
    TextField,
    OneToOneField,
    ForeignKey,
    ManyToManyField,
    CASCADE
)
from users.models import Manager
from django.db.models.fields.files import ImageField

# Create your models here.


class Enterprise(Model):
    """Clase que representa una Establecimiento"""

    name = CharField(max_length=45, help_text='nombre')
    historical_review = TextField(
        null=True,
        blank=True,
        help_text='reseña historica'
    )
    city = CharField(max_length=75, help_text='ubicación')
    location = CharField(max_length=250, help_text='ubicación')
    business_hours = CharField(
        max_length=500,
        null=True,
        blank=True,
        help_text='horario de atención',
    )
    status = BooleanField(default=True, help_text='estado')
    created = DateTimeField(auto_now_add=True, help_text='creado')

    
    image = ImageField(
        upload_to='upload/images/enterprises',
        null=True,
        blank=True,
        help_text='imagen',
    )
    # Relaciones
    # image = OneToOneField(
    #     'products.Image',
    #     null=True,
    #     blank=True,
    #      on_delete=CASCADE,
    #      help_text='imagen'
    #  )
    managers = ManyToManyField(
        'users.Manager',
        through='Management',
        related_name='enterprises',
        help_text='administradores de establecimiento'
    )

    def __str__(self) -> str:
        """
        Función que representa al objeto
        cuando es recuperado

        """
        return self.name

    # def _init_(self):
    #     return self.name


class Management(Model):
    """
    Clase que representa la Gestión entre
    Establecimientos y Administradores de Establecimientos
    """

    date = DateTimeField(auto_now_add=True, help_text='fecha')
    status = BooleanField(default=True, help_text='estado')

    # Relaciones
    enterprise = ForeignKey(
        Enterprise,
        related_name='managements',
        on_delete=CASCADE,
        help_text='establecimiento'
    )
    manager = ForeignKey(
        Manager,
        related_name='managements',
        on_delete=CASCADE,
        help_text='administrador del establecimiento'
    )

    def __str__(self) -> str:
        """
        Función que representa al objeto
        cuando es recuperado
        """

        return self.date.strftime('%Y-%m-%d %H:%M')
