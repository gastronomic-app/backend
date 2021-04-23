from graphene import Field
from graphene import Mutation

from users.models import Client
from api_graphql.data.client.types import ClientNode
from api_graphql.data.client.inputs import CreateClientInput

# Create your mutations here


class CreateClient(Mutation):
    client = Field(ClientNode)

    class Arguments:
        input = CreateClientInput(required=True)

    def mutate(self, info, input: CreateClientInput):
        client = Client.objects.create(**vars(input))

        return CreateClient(client=client)
