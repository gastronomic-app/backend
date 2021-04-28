from graphene import Field
from graphene import Mutation
from graphene.types.scalars import ID
from graphql import GraphQLError
from graphql_relay.node.node import from_global_id

from reviews.models import Review
from api_graphql.data.review.types import ReviewNode
from api_graphql.data.review.inputs import CreateReviewInput
from api_graphql.data.review.inputs import UpdateReviewInput
from api_graphql.data.review.inputs import DeleteReviewInput
from api_graphql.utils import delete_attributes_none
from api_graphql.utils import transform_global_ids


class CreateReview(Mutation):
    # Clase para crear una valoración
    review = Field(ReviewNode)

    class Arguments:
        input = CreateReviewInput(required=True)

    def mutate(self, info, input):
        import pdb; pdb.set_trace()
        input = delete_attributes_none(**vars(input))
        input = transform_global_ids(**input) #Transformacion de Ids
        review = Review.objects.create(**input)

        return CreateReview(review=review)


class UpdateReview(Mutation):
    # Clase para realizar la actualización de un pedido
    review = Field(ReviewNode)

    class Arguments:
        input = UpdateReviewInput(required=True)

    def mutate(self, info, input):
        input = delete_attributes_none(**vars(input))
        input = transform_global_ids(**input)

        Review.objects.filter(pk=input.get('id')).update(**input)
        review = Review.objects.get(pk=input.get('id'))

        return UpdateReview(review=review)
