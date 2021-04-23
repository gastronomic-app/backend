from graphene.relay import Node
from graphene_django import DjangoObjectType

from users.models import Client
from api_graphql.connections import TotalCountConnection

# Create your objects types here.


class ClientNode(DjangoObjectType):

    class Meta:
        model = Client 
        filter_fields = {
            'names': ['exact', 'icontains', 'istartswith'],
            'lastnames': ['exact', 'icontains', 'istartswith'],
            'location': ['exact', 'icontains', 'istartswith'],
            'telephone': ['exact', 'icontains', 'istartswith'],
            'role': ['exact'],
            'created': ['exact'],
            'updated': ['exact']
        }
        interfaces = (Node, )
        connection_class = TotalCountConnection
