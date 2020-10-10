from apps.dht11.models import DHT11
from rest_framework import serializers


class DHT11Serializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = DHT11
        fields = [
            'timestamp',
            'temperature',
            'humidity',
        ]
