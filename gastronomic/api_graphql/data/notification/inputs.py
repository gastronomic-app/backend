from graphene import InputObjectType
from graphene.types.scalars import ID
from graphene.types.scalars import String
from graphene.types.scalars import Boolean

# Create your inputs types here.


class CreateNotificationInput(InputObjectType):
    """
    Clase que encapsula los datos necesarios para la
    creacion de la notificación
    """

    title = String(required=True)
    message = String(required=True)

    # Relaciones
    user_id = String(required=True)


class UpdateNotificationInput(InputObjectType):
    """
    Clase que encapsula los datos necesarios
    para la actualización de la notificación
    """

    id = ID(required=True)
    title = String()
    message = String()
    read = Boolean()


    # Relaciones
    user_id = String()
