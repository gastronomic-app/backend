from graphene import (
    ID,
    String,
    InputObjectType
)

# Create your inputs types here.


class CreateImageInput(InputObjectType):
    """
    Clase que encapsula los datos necesarios
    para la creación de imagenes
    """
    url = String(required=True)

    # Relaciones
    product_id = ID(required=True)


class UpdateImageInput(InputObjectType):
    """
    Clase que encapsula los datos necesarios
    para la actualización de imagenes
    """
    id = ID(required=True)
    url = String() 
    
    # Relaciones
    product_id=ID()