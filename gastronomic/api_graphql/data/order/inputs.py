from graphene import InputObjectType
from graphene.types.scalars import Int
from graphene.types.scalars import ID
from graphene.types.scalars import String

# Create your inputs here


class CreateOrderInput(InputObjectType):
    """
    Clase que encapsula los datos
    necesarios para la creación de Pedido
    """

    estimated_time = String(required=True)
    location = String(required=True)
    complaint = String()

    # Relaciones
    client_id = ID(required=True)
    courier_id = ID()


class UpdateOrderInput(InputObjectType):
    """
    Clase para encapsular los datos
    necesarios para la actualización de pedido
    """

    id = ID(required=True)

    status = String()
    estimated_time = String()
    location = String()
    complaint = String()

    # Relaciones
    client_id = ID()
    courier_id = ID()
