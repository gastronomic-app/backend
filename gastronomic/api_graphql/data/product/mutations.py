from collections import _OrderedDictValuesView
from graphene import Field
from graphene import Mutation
from graphene.types.scalars import ID
from graphql import GraphQLError
from graphql_relay.node.node import from_global_id

from products.models import Product
from api_graphql.data.product.types import ProductNode
from api_graphql.data.product.inputs import CreateProductInput
from api_graphql.data.product.inputs import UpdateProductInput
from api_graphql.data.product.inputs import AddAccompanimentInput
from api_graphql.data.product.inputs import DeleteAccompanimentInput
from api_graphql.utils import delete_attributes_none
from api_graphql.utils import transform_global_ids


# Create your mutations here


class CreateProduct(Mutation):
    """Clase para crear productos"""
    product = Field(ProductNode)

    class Arguments:
        input = CreateProductInput(required=True)

    def mutate(self, info, input):
        # Elimina nulos y transforma el id
        input = delete_attributes_none(**vars(input))
        input = transform_global_ids(**input)
        
        product = Product.objects.create(**input)

        return CreateProduct(product=product)


class UpdateProduct(Mutation):
    """Clase para actualizar productos"""
    product = Field(ProductNode)

    class Arguments:
        input = UpdateProductInput(required=True)

    def mutate(self, info, input):
        # Elimina nulos y transforma el id
        input = delete_attributes_none(**vars(input))
        input = transform_global_ids(**input)

        Product.objects.filter(pk=input.get('id')).update(**input)
        product = Product.objects.get(pk=input.get('id'))

        return UpdateProduct(product=product)

class ChangeState(Mutation):
    """Clase para desahabilitar productos"""
    product = Field(ProductNode)

    class Arguments:
        input = ID(required=True)

    def mutate(self, info, input):
        input = from_global_id(input)[1]

        product = Product.objects.get(pk=input)
        product.active = product.active != True
        product.save()
        return ChangeState(product=product)

class DeleteProduct(Mutation):
    """Clase para eliminar productos"""
    product = Field(ProductNode)

    class Arguments:
        input = ID(required=True)

    def mutate(self, info, input):
        # Transforma el id
        input = from_global_id(input)[1]

        try:
            product = Product.objects.get(pk=input)
            Product.objects.filter(pk=input).delete()
        except Product.DoesNotExist:
            raise GraphQLError('Product does not delete')

        return CreateProduct(product=product)

class AddAccompaniment(Mutation):
    """Clase para añadir acompañamiento"""
    product = Field(ProductNode)

    class Arguments:
        input = AddAccompanimentInput(required=True)

    def mutate(self, info, input):
        # Elimina nulos y transforma el id
        input = delete_attributes_none(**vars(input))
        input = transform_global_ids(**input)
        product = Product.objects.get(pk=input.get('from_product_id'))

        Product.accompaniments.through.objects.create(
                from_product_id=product.pk,
                to_product_id=input.pop('to_product_id')
            )
        return AddAccompaniment(product=product)

    
class DeleteAccompaniment(Mutation):
    """Clase para eliminar acompañamientos"""
    product = Field(ProductNode)

    class Arguments:
        input = DeleteAccompanimentInput(required=True)

    def mutate(self, info, input):
        # Elimina nulos y transforma el id
        input = delete_attributes_none(**vars(input))
        input = transform_global_ids(**input)
        product = Product.objects.get(pk=input.get('from_product_id'))
        for accomp in Product.accompaniments.through.objects.filter(from_product_id=input.get('from_product_id'),to_product_id=input.get('to_product_id')):
            accomp.delete()
        return DeleteAccompaniment(product=product)
