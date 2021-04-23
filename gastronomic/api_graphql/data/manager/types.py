from graphene.relay import Node
from graphene_django import DjangoObjectType

from enterprises.models import Manager
from api_graphql.connections import TotalCountConnection

# Create your objects types here.


class ManagerNode(DjangoObjectType):

    class Meta:
        model = Manager 
        filter_fields = {
            'date': ['exact'],
            'status': ['exact', 'icontains', 'istartswith']
        }
        interfaces = (Node, )
        connection_class = TotalCountConnection
