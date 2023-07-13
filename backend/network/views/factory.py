from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics

from network.filters import FactoryFilter
from network.models import Factory
from network import serializers


class FactoryCreateView(generics.CreateAPIView):
    queryset = Factory.objects.all()
    serializer_class = serializers.FactoryCreateUpdateSerializer


class FactoryListView(generics.ListAPIView):
    queryset = Factory.objects.all()
    serializer_class = serializers.FactorySerializer
    filterset_class = FactoryFilter


class FactoryDetailDeleteView(generics.RetrieveDestroyAPIView):
    queryset = Factory.objects.all()
    serializer_class = serializers.FactorySerializer


class FactoryUpdateView(generics.UpdateAPIView):
    queryset = Factory.objects.all()
    serializer_class = serializers.FactoryCreateUpdateSerializer
