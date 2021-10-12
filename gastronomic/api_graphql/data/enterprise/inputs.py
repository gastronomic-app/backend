from graphene import InputObjectType
from graphene.types.scalars import ID
from graphene.types.scalars import String
from graphene.types.scalars import Boolean
from graphene_file_upload.scalars import Upload
# Create your inputs types here.


class CreateEnterpriseInput(InputObjectType):
    """
    Clase que encapsula los datos necesarios
    para la creación de establecimientos
    """

    name = String(required=True)
    historical_review = String()
    location = String(required=True)
    city = String(required=True)
    business_hours = String()
    status = Boolean()

    # Relaciones
    image = Upload()


class UpdateEnterpriseInput(InputObjectType):
    """
    Clase que encapsula los datos necesarios
    para la actualización de establecimientos
    """

    id = ID(required=True)
    name = String()
    historical_review = String()
    location = String()
    city = String(required=True)
    business_hours = String()
    status = Boolean()
    # Relaciones
    image = Upload()
