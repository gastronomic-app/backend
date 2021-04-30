from graphene import Field
from graphene import Mutation
from graphene.types.scalars import ID
from graphql import GraphQLError
from graphql_relay.node.node import from_global_id

from products.models import Image
from api_graphql.data.image.types import ImageNode
from api_graphql.data.image.inputs import CreateImageInput
from api_graphql.data.image.inputs import UpdateImageInput
from api_graphql.utils import delete_attributes_none
from api_graphql.utils import transform_global_ids


# Create your mutations here

class CreateImage(Mutation):
    """Clase para crear imagenes"""
    image = Field(ImageNode)

    class Arguments:
        input = CreateImageInput(required=True)

    def mutate(self, info, input):
        # Elimina nulos y transforma el id
        input = delete_attributes_none(**vars(input))
        input = transform_global_ids(**input)
        
        image = Image.objects.create(**input)

        return CreateImage(image=image)


class UpdateImage(Mutation):
    """Clase para actualizar imagenes"""
    image = Field(ImageNode)

    class Arguments:
        input = UpdateImageInput(required=True)

    def mutate(self, info, input):
        # Elimina nulos y transforma el id
        input = delete_attributes_none(**vars(input))
        input = transform_global_ids(**input)

        Image.objects.filter(pk=input.get('id')).update(**input)
        image = Image.objects.get(pk=input.get('id'))

        return UpdateImage(image=image)


class DeleteImage(Mutation):
    """Clase para eliminar imagenes"""
    image = Field(ImageNode)

    class Arguments:
        input = ID(required=True)

    def mutate(self, info, input):
        # Transforma el id
        input = from_global_id(input)[1]

        try:
            image = Image.objects.get(pk=input)
            Image.objects.filter(pk=input).delete()
        except Image.DoesNotExist:
            raise GraphQLError('Image does not delete')

        return CreateImage(image=image)



