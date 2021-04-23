from graphene import ObjectType
from graphene.relay import Node
from graphene_django.filter import DjangoFilterConnectionField

# from .data.image.types import ImageNode
from .data.order.types import OrderNode
from .data.detail.types import DetailNode
from .data.client.types import ClientNode
from .data.courier.types import CourierNode
from .data.product.types import ProductNode
from .data.manager.types import ManagerNode
from .data.delivery.types import DeliveryNode
from .data.client.mutations import CreateClient
from .data.enterprise.types import EnterpriseNode
from .data.enterprise.mutations import CreateEnterprise, UpdateEnterprise, DeleteEnterprise
from .data.product.mutations import CreateProduct, UpdateProduct, DeleteProduct


# Schema definition

class Query(ObjectType):

    """Endpoint para consultar registros"""
    delivery = Node.Field(DeliveryNode)
    courier = Node.Field(CourierNode)
    client = Node.Field(ClientNode)
    enterprise = Node.Field(EnterpriseNode)
    order = Node.Field(OrderNode)
    product = Node.Field(ProductNode)
    manager = Node.Field(ManagerNode)
    detail = Node.Field(DetailNode)
    # image = Node.Field(ImageNode)

    all_deliveries = DjangoFilterConnectionField(DeliveryNode)
    all_couriers = DjangoFilterConnectionField(CourierNode)
    all_clients = DjangoFilterConnectionField(ClientNode)
    all_enterprises = DjangoFilterConnectionField(EnterpriseNode)
    all_orders = DjangoFilterConnectionField(OrderNode)
    all_products = DjangoFilterConnectionField(ProductNode)
    all_managers = DjangoFilterConnectionField(ManagerNode)
    all_details = DjangoFilterConnectionField(DetailNode)
    # all_images = DjangoFilterConnectionField(ImageNode)
    
    
class Mutation(ObjectType):
    """Endpoint para crear, actualizar y eliminar registros"""

    create_client = CreateClient.Field()
    create_enterprise = CreateEnterprise.Field()
    create_product = CreateProduct.Field()

    update_enterprise = UpdateEnterprise.Field()
    update_product = UpdateProduct.Field()

    delete_enterprise = DeleteEnterprise.Field()
    delete_product = DeleteProduct.Field()
