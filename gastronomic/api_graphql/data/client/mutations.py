from graphene import Field
from graphene import Mutation
from graphene.types.scalars import ID
from profiles.models import UserProfile

from users.models import Client, Contact
from api_graphql.data.client.types import ClientNode
from api_graphql.data.user.types import UserNode
from api_graphql.data.client.inputs import CreateClientInput, RememberPasswordInput
from api_graphql.data.client.inputs import UpdateClientInput
from api_graphql.utils import delete_attributes_none
from api_graphql.utils import transform_global_ids
from users.views import remember,signup
# Create your mutations here


class CreateClient(Mutation):
    """Clase para crear clientes"""

    client = Field(ClientNode)

    class Arguments:
        input = CreateClientInput(required=True)

    def mutate(self, info, input: CreateClientInput):
        input = vars(input)
        client = Client(
            email=input.pop('email'),
            password=input.pop('password'),
            is_alternative = input.pop('is_alternative')
        )
        input['user'] = client
        contact = Contact(**input)
        client.is_active=False
        client.save()
        contact.save()
        signup(client, info.context)

        return CreateClient(client=client)


class UpdateClient(Mutation):
    """Clase para actualizar clientes"""

    client = Field(UserNode)

    class Arguments:
        input = UpdateClientInput(required=True)

    def mutate(self, info, input):
        # Elimina nulos y transforma el id
        input = delete_attributes_none(**vars(input))
        input = transform_global_ids(**input)
        
        UserProfile.objects.filter(pk=input.get('id')).update(**input)
        client = UserProfile.objects.get(pk=input.get('id'))
        client.set_password(client.password)
        client.save()

        return UpdateClient(client=client)

class RememberPasswordClient(Mutation):
    """Clase para actualizar clientes"""

    client = Field(UserNode)

    class Arguments:
        input = RememberPasswordInput(required=True)

    def mutate(self, info, input):
        client = UserProfile.objects.get(email=input)
        if (client.is_alternative==False):
            if (client.is_active):
                remember(client, info.context)
            else:
                return "Usuario inactivo"
        return RememberPasswordClient(client=client)

class ActivateClient(Mutation):
    """Clase para crear clientes"""

    client = Field(ClientNode)

    class Arguments:
        input = RememberPasswordInput(required=True)

    def mutate(self, info, input: RememberPasswordInput):
        client = Client.objects.get(email=input)
        signup(client, info.context)
        return ActivateClient(client=client)
