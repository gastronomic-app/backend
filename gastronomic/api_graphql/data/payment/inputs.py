from graphene import (
    ID,
    String,
    InputObjectType
)

# Create your inputs types here.

class CreatePaymentInput(InputObjectType):
    """
    Clase que encapsula los datos necesarios
    para la creación de pagos
    """
    payment_type = String(required=True)
    payment_value = String(required=True)
    
    # Relaciones
    delivery_id = ID(required=True)
    

class UpdatePaymentInput(InputObjectType):
    """
    Clase que encapsula los datos necesarios
    para la actualización de pagos
    """
    id = ID(required=True)
    payment_type = String()
    payment_value = String()