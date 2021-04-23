import os
import base64
from graphene import String
from graphene.relay import Node
from graphene_django import DjangoObjectType

from products.models import Image
from api_graphql.connections import TotalCountConnection

# Create your objects types here.


# class ImageNode(DjangoObjectType):
#     """
#     Clase que representa el componente básico que se utiliza
#     para definir la relación entre los campos del esquema
#     y cómo se recuperan los datos.
#     """

#     class Meta:
#         model = Image
#         filter_fields = {
#             'url': ['exact']
#         }
#         interfaces = (Node, )
#         connection_class = TotalCountConnection

    # base64file = String()

    # def resolve_base64file(self, info):
    #     if self is not None and self.image and hasattr(self.image, 'url'):
    #         if os.path.isfile(self.image.url):
    #             return base64.b64encode(self.image.read())
    #         else:
    #             return 'File not found'
    #     return ''
