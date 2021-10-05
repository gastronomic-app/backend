from graphene import Field
from graphene import Mutation
from graphene.types.scalars import ID
from graphql import GraphQLError
from graphql_relay.node.node import from_global_id

from payments.models import Payment
from api_graphql.data.payment.types import PaymentNode
from api_graphql.data.payment.inputs import CreatePaymentInput
from api_graphql.data.payment.inputs import UpdatePaymentInput
from api_graphql.utils import delete_attributes_none
from api_graphql.utils import transform_global_ids


# Create your mutations here


class CreatePayment(Mutation):
    """Clase para crear pagos"""
    payment = Field(PaymentNode)

    class Arguments:
        input = CreatePaymentInput(required=True)

    def mutate(self, info, input):
        # Elimina nulos y transforma el id
        input = delete_attributes_none(**vars(input))
        input = transform_global_ids(**input)

        payment = Payment.objects.create(**input)

        return CreatePayment(payment=payment)


class UpdatePayment(Mutation):
    """Clase para actualizar pagos"""
    payment = Field(PaymentNode)

    class Arguments:
        input = UpdatePaymentInput(required=True)

    def mutate(self, info, input):
        # Elimina nulos y transforma el id
        input = delete_attributes_none(**vars(input))
        input = transform_global_ids(**input)

        Payment.objects.filter(pk=input.get('id')).update(**input)
        payment = Payment.objects.get(pk=input.get('id'))

        return UpdatePayment(payment=payment)


class DeletePayment(Mutation):
    """Clase para eliminar pagos"""
    payment = Field(PaymentNode)

    class Arguments:
        input = ID(required=True)

    def mutate(self, info, input):
        # Transforma el id
        input = from_global_id(input)[1]

        try:
            
            payment = Payment.objects.get(pk=input)
            Payment.objects.filter(pk=input).delete()
        except Payment.DoesNotExist:
            raise GraphQLError('Payment does not delete')

        return CreatePayment(payment=payment)
