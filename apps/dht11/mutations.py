import graphene
from graphene_django.rest_framework.mutation import SerializerMutation
from .types import DHT11Type
from .models import DHT11
from .serializers import DHT11Serializer


class CreateDHT11Mutation(SerializerMutation):
    class Meta:
        serializer_class = DHT11Serializer


# class CreateDHT11Mutation(graphene.Mutation):
#    class Arguments:
#        temperature = graphene.Float()
#        humidity = graphene.Float()
#    dht11 = graphene.Field(DHT11Type)

#    def mutate(self, info, temperature, humidity):
#        dht11 = DHT11.objects.create(
#            temperature=temperature,
#            humidity=humidity
#        )
#        return CreateDHT11Mutation(dht11=dht11)


class EditDHT11Mutation(graphene.Mutation):
    class Arguments:
        id = graphene.ID()
        temperature = graphene.Float()
        humidity = graphene.Float()

    dht11 = graphene.Field(DHT11Type)

    def mutate(self, info, id, temperature, humidity):
        dht11_instance = DHT11.objects.get(pk=id)
        if dht11_instance:
            dht11_instance.temperature = temperature
            dht11_instance.humidity = humidity
            dht11_instance.save()
            return EditDHT11Mutation(dht11=dht11_instance)
        return EditDHT11Mutation(dht11=None)


class DeleteDHT11Mutation(graphene.Mutation):
    class Arguments:
        id = graphene.ID()
    dht11 = graphene.Field(DHT11Type)

    def mutate(self, info, id):
        dht11_instance = DHT11.objects.get(id=id)
        if dht11_instance is not None:
            dht11_instance.delete()
            return DeleteDHT11Mutation(dht11=dht11_instance)
        return DeleteDHT11Mutation(dht11=None)
