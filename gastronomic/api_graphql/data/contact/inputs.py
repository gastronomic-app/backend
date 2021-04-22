from graphene import InputObjectType
from graphene.types.scalars import ID
from graphene.types.scalars import String
from graphene.types.scalars import Boolean
from graphene.types.datetime import DateTime

class CreateContactInput(InputObjectType):
    names = String(required=True)
    lastnames = String(required=True)
    location = String(Required=True)
    telephone = String(Required=True)
    license_plate = String()
    created = DateTime(Required=True)
    updated = DateTime(Required=True)
    user_id = ID(Required=True)

class UpdateContactInput(InputObjectType):
    id=ID(Required=True)
    names = String()
    lastnames = String()
    location = String()
    telephone = String()
    license_plate = String()
    created = DateTime()
    updated = DateTime()
    user_id = ID()
