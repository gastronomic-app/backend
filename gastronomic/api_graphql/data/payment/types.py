from graphene.relay import Node
from graphene_django import DjangoObjectType

from api_graphql.connections import TotalCountConnection
from payments.models import Payment

# Create your objects types here.


class PaymentNode(DjangoObjectType):

    class Meta:
        model = Payment 
        filter_fields = {
            'payment_type': ['exact', 'icontains', 'istartswith'],
            'payment_value': ['exact'],
        }
        interfaces = (Node, )
        connection_class = TotalCountConnection
