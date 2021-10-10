from graphene import Mutation
from graphene import Field

from notifications.models import Notification
from api_graphql.data.notification.types import NotificationNode
from api_graphql.data.notification.inputs import CreateNotificationInput
from api_graphql.data.notification.inputs import UpdateNotificationInput

from api_graphql.utils import transform_global_ids
from api_graphql.utils import delete_attributes_none


class CreateNotification(Mutation):
    """Clase para crear notificaciones"""

    notification = Field(NotificationNode)

    class Arguments:
        input = CreateNotificationInput(required=True)

    def mutate(self, info, input):
        input = delete_attributes_none(**vars(input))
        input = transform_global_ids(**input)

        notification = Notification.objects.create(**input)

        return CreateNotification(notification=notification)


class UpdateNotification(Mutation):
    """Clase para actualizar notificaciones"""

    notification = Field(NotificationNode)

    class Arguments:
        input = UpdateNotificationInput(required=True)

    def mutate(self, info, input):
        input = delete_attributes_none(**vars(input))
        input = transform_global_ids(**input)

        Notification.objects.filter(pk=input.get("id")).update(**input)
        notification = Notification.objects.get(pk=input.get("id"))

        return UpdateNotification(notification=notification)
