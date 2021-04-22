from graphene import InputObjectType
from graphene.types.scalars import ID
from graphene.types.scalars import String
from graphene.types.scalars import Boolean

class CreateClientInput(InputObjectType):
    """
    Clase que encapsula los datos necesarios para la 
    creacion de clientes
    """
    email = String(required=True)
    password = String(required=True)
    type = String(required=True)
    is_active = Boolean(required=True)
    is_staff = Boolean(required=True)
    is_superuser = Boolean(required=True)
    last_login = String()

class UpdateClientInput(InputObjectType):
    email = String(required=True)
    password = String()
    type = String()
    is_active = Boolean()
    is_staff = Boolean()
    is_superuser = Boolean()
    last_login = String()