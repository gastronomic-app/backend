from graphene.relay import Node
from graphene_django import DjangoObjectType

from api_graphql.connections import TotalCountConnection
from reviews.models import Review

# Create your objects types here.


class ReviewNode(DjangoObjectType):

    class Meta:
        model = Review 
        filter_fields = {
            'quality_service': ['exact', 'icontains', 'istartswith'],
            'presentation': ['exact', 'icontains', 'istartswith'],
            'preparation': ['exact', 'icontains', 'istartswith'],
            'ingredients': ['exact', 'icontains', 'istartswith'],
            'price': ['exact', 'icontains', 'istartswith'],
            'textures': ['exact', 'icontains', 'istartswith'],
            'cooking_point': ['exact', 'icontains', 'istartswith'],
            'comments': ['exact', 'icontains', 'istartswith'],
            'date': ['exact', 'icontains', 'istartswith']
        }
        interfaces = (Node, )
        connection_class = TotalCountConnection
