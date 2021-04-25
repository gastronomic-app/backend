from graphene import Field
from graphene import Mutation
from graphene.types.scalars import ID
from graphql_relay.node.node import from_global_id

from users.models import Client
from api_graphql.data.client.types import ClientNode
from api_graphql.data.client.inputs import CreateClientInput
from api_graphql.data.client.inputs import UpdateClientInput
from api_graphql.utils import delete_attributes_none
from api_graphql.utils import transform_global_ids

# Create your mutations here


class CreateClient(Mutation):
    """Clase para crear clientes"""

    client = Field(ClientNode)

    class Arguments:
        input = CreateClientInput(required=True)

    def mutate(self, info, input: CreateClientInput):
        client = Client.objects.create(**vars(input))

        return CreateClient(client=client)


class UpdateClient(Mutation):
    """Clase para actualizar clientes"""

    client = Field(ClientNode)

    class Arguments:
        input = UpdateClientInput(required=True)

    def mutate(self, info, input):
        # Elimina nulos y transforma el id
        input = delete_attributes_none(**vars(input))
        input = transform_global_ids(**input)

        Client.objects.filter(pk=input.get('id')).update(**input)
        client = Client.objects.get(pk=input.get('id'))

        return UpdateClient(client=client)
