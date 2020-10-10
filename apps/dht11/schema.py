import graphene
#from graphene import relay
from .models import DHT11
from .types import DHT11Type, DHT11Filter
from .mutations import EditDHT11Mutation, CreateDHT11Mutation, DeleteDHT11Mutation
'''
from graphene_django.filter import DjangoFilterConnectionField
class Query(graphene.ObjectType):
    dht11s = DjangoFilterConnectionField(DHT11Type,
                                         filterset_class=DHT11Filter,
                                         first=graphene.Int(),
                                         skip=graphene.Int())

    def resolve_dht11s(self, info, **kwargs):
        if not info.context.user.is_authenticated():
            return DHT11.objects.none()
        else:
            qs = DHT11.objects.all()
            if kwargs.skip:
                qs = qs[kwargs.skip:]
            if kwargs.first:
                qs = qs[:kwargs.first]
            return qs

    dht11est = graphene.Field(DHT11Type)

    def resolve_dht11est(self, info, **kwargs):
        return DHT11.objects.latest('timestamp')
'''


class Query(graphene.ObjectType):
    dht11s = graphene.List(DHT11Type)
    dht11est = graphene.Field(DHT11Type)

    def resolve_dht11s(self, info, **kwargs):
        return DHT11.objects.all()

    def resolve_dht11est(self, info, **kwargs):
        return DHT11.objects.latest('timestamp')


class Mutation(graphene.ObjectType):
    create_dht11 = CreateDHT11Mutation.Field()
    update_dht11 = EditDHT11Mutation.Field()
    delete_dht11 = DeleteDHT11Mutation.Field()


schema = graphene.Schema(query=Query, mutation=Mutation)
