from rest_framework import generics

from network.filters import RetailNetworkFilter
from network.models import RetailNetwork
from network import serializers


class RetailNetworkCreateView(generics.CreateAPIView):
    queryset = RetailNetwork.objects.all()
    serializer_class = serializers.RetailNetworkCreateSerializer


class RetailNetworkListView(generics.ListAPIView):
    queryset = RetailNetwork.objects.all()
    serializer_class = serializers.RetailNetworkSerializer
    filterset_class = RetailNetworkFilter


class RetailNetworkDetailDeleteView(generics.RetrieveDestroyAPIView):
    queryset = RetailNetwork.objects.all()
    serializer_class = serializers.RetailNetworkSerializer


class RetailNetworkUpdateView(generics.UpdateAPIView):
    queryset = RetailNetwork.objects.all()
    serializer_class = serializers.RetailNetworkUpdateSerializer