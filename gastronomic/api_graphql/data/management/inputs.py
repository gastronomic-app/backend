from graphene import InputObjectType
from graphene.types.scalars import Boolean, String
from graphene.types.scalars import ID


class CreateManagementInput(InputObjectType):
    """
    Clase que encapsula los datos necesarios
    para la creación de Administradores
    """
    status = Boolean()
    #Relaciones
    enterprise_id = ID(required = True)
    management_Id = ID(required = True)

class UpdateManagementInput(InputObjectType):
    """
    Clase que encapsula los datos necesarios
    para la creación de Administradores
    """
    id = ID(required = True)
    status = Boolean(required = True)
    #Relaciones
    enterprise_id = ID(required = True)
    management_id = ID(required = True)
