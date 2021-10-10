from graphene.relay import Node
from graphene_django import DjangoObjectType

from notifications.models import Notification
from api_graphql.connections import TotalCountConnection

# Create your objects types here.


class NotificationNode(DjangoObjectType):
    """
    Clase que representa el componente básico que se utiliza
    para definir la relación entre los campos del esquema
    y cómo se recuperan los datos.
    """

    class Meta:
        model = Notification
        filter_fields = {
            'title': ['exact', 'icontains', 'istartswith'],
            'message': ['exact', 'icontains', 'istartswith'],
            'created': ['exact', 'icontains', 'istartswith']
        }
        interfaces = (Node, )
        connection_class = TotalCountConnection
