from graphene import ID
from graphene import String
from graphene import InputObjectType
from graphene.types.scalars import Boolean


# Create your inputs types here.


class CreateClientInput(InputObjectType):
    name = String(required=True)
    location = String(required=True)
    telephone = String(required=True)
