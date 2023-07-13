from rest_framework import generics

from network.filters import IndividualEntrepreneurFilter
from network.models import IndividualEntrepreneur
from network import serializers


class IndividualEntrepreneurCreateView(generics.CreateAPIView):
    queryset = IndividualEntrepreneur.objects.all()
    serializer_class = serializers.IndividualEntrepreneurCreateSerializer


class IndividualEntrepreneurListView(generics.ListAPIView):
    queryset = IndividualEntrepreneur.objects.all()
    serializer_class = serializers.IndividualEntrepreneurSerializer
    filterset_class = IndividualEntrepreneurFilter


class IndividualEntrepreneurDetailDeleteView(generics.RetrieveDestroyAPIView):
    queryset = IndividualEntrepreneur.objects.all()
    serializer_class = serializers.IndividualEntrepreneurSerializer


class IndividualEntrepreneurUpdateView(generics.UpdateAPIView):
    queryset = IndividualEntrepreneur.objects.all()
    serializer_class = serializers.IndividualEntrepreneurUpdateSerializer
