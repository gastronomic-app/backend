from graphene import InputObjectType
from graphene.types.scalars import ID
from graphene.types.scalars import String

# Create your inputs types here.


class CreateContactInput(InputObjectType):
    """
    Clase que encapsula los datos necesarios
    para la creación de contacto
    """

    names = String(required=True)
    lastnames = String(required=True)
    city = String(required=True)
    location = String(required=True)
    telephone = String(required=True)
    license_plate = String()

    # Relaciones
    user_id = ID(required=True)


class UpdateContactInput(InputObjectType):
    """
    Clase que encapsula los datos necesarios
    para la actualización de contacto
    """

    id = ID(required=True)
    names = String()
    lastnames = String()
    city = String()
    location = String()
    telephone = String()
    license_plate = String()

    # Relaciones
    user_id = ID()
