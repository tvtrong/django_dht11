import django_filters
from graphene_django import DjangoObjectType
from .models import DHT11


class DHT11Filter(django_filters.FilterSet):
    timestamp__exact = django_filters.CharFilter(
        field_name='timestamp', lookup_expr=['iexact'])
    temperature__gt = django_filters.NumberFilter(
        field_name='temperature', lookup_expr='gt')

    class Meta:
        model = DHT11
        fields = ['timestamp', 'temperature', 'humidity']


class DHT11Type(DjangoObjectType):
    class Meta:
        model = DHT11
        #exclude = ('timestamp')
        #fields = ('temperature', 'humidity')
        #fields = '__all__'
