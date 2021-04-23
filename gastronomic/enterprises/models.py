from django.db import models

from users.models import EstablishmentManager

# Create your models here.


class Enterprise(models.Model):
    """Clase que representa una Empresa"""

    name = models.CharField(max_length=45, help_text='nombre')
    historical_review = models.TextField(null=True, blank=True, help_text='reseña historica')
    location = models.CharField(max_length=45, help_text='ubicación')
    business_hours = models.CharField(max_length=45, null=True, blank=True, help_text='horario de atención')
    status = models.BooleanField(default=True, help_text='estado')
    created = models.DateTimeField(auto_now_add=True, help_text='creado')

    # Relaciones
    image = models.OneToOneField('products.Image', null=True, blank=True, on_delete=models.CASCADE, help_text='imagen')

    def __str__(self) -> str:
        """
        Función que representa al objeto
        cuando es recuperado

        Retorna:
            String: representa al objeto
        """
        return self.name


class Manager(models.Model):
    """Clase intermedia entre empresas y administradores de establecimientos"""

    date = models.DateTimeField(auto_now_add=True, help_text='fecha')
    status = models.BooleanField(default=True, help_text='estado')

    # Relaciones
    enterprise = models.ForeignKey(
        'Enterprise',
        related_name='managers',
        on_delete=models.CASCADE,
        help_text='empresa'
    )
    establishment_manager = models.ForeignKey(
        EstablishmentManager,
        related_name='managers',
        on_delete=models.CASCADE,
        help_text='administrador del establecimiento'
    )

    def __str__(self) -> str:
        """
        Función que representa al objeto
        cuando es recuperado

        Retorna:
            String: representa al objeto
        """
        return self.date.strftime('%Y-%m-%d %H:%M')
