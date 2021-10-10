from graphene import Field
from graphene import Mutation

from enterprises.models import Management

from api_graphql.data.management.types import ManagementNode
from api_graphql.data.management.inputs import CreateManagementInput
from api_graphql.data.management.inputs import UpdateManagementInput
from api_graphql.utils import transform_global_ids
from api_graphql.utils import delete_attributes_none


class CreateManagement(Mutation):
    """Clase para crear Managements"""

    management = Field(ManagementNode)

    class Arguments:
        input = CreateManagementInput(required=True)

    def mutate(self,info,input):
        input = delete_attributes_none(**vars(input))
        input = transform_global_ids(**input)
        management = Management.objects.create(**input)
        return CreateManagement(management=management)


class UpdateManagement(Mutation):
    """
    Clase para actualizar Managements
    """
    management = Field(ManagementNode)
    class Arguments:
        input = UpdateManagementInput(required = True)
        
    def mutate(self,info,input):
        input = delete_attributes_none(**vars(input))
        input = transform_global_ids(**input)

        Management.objects.filter(pk=input.get('id'))
        management = Management.objects.get(pk=input.get('id'))

        return UpdateManagement(management=management)
