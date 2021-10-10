from django.db.models import (
    Model,
    CharField,
    TextField,
    DateTimeField,
    ForeignKey,
    CASCADE,
)

from profiles.models import UserProfile

# Create your models here.


class Notification(Model):
    """Clase que representa una Notificación"""

    title = CharField(max_length=45, help_text='titulo')
    message = TextField(help_text='mensaje')
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
