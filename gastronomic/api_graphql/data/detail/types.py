from graphene.relay import Node
from graphene_django import DjangoObjectType

from orders.models import Detail
from api_graphql.connections import TotalCountConnection

# Create your objects types here.


class DetailNode(DjangoObjectType):

    class Meta:
        model = Detail
        filter_fields = {
            'quantity': ['exact']
        }
        interfaces = (Node, )
        connection_class = TotalCountConnection
