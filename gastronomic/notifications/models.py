from django.db.models import (
    CASCADE,
    BooleanField,
    CharField,
    DateTimeField,
    ForeignKey,
    Model,
    TextField
)

from profiles.models import UserProfile

# Create your models here.


class Notification(Model):
    """Clase que representa una Notificación"""

    title = CharField(max_length=45, help_text='titulo')
    message = TextField(help_text='mensaje')
    read = BooleanField(default=False, help_text='notificación leida')
    created = DateTimeField(auto_now_add=True, help_text='fecha creación')

    # Relaciones
    user = ForeignKey(
        UserProfile,
        related_name='notifications',
        on_delete=CASCADE,
        help_text='usuario'
    )

    def __str__(self) -> str:
        return self.title
