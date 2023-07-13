import django_filters

from network.models import Factory, RetailNetwork, IndividualEntrepreneur


class CountryFilter(django_filters.FilterSet):
    country = django_filters.CharFilter(field_name='contact__country', lookup_expr='istartswith')


class FactoryFilter(CountryFilter):
    class Meta:
        model = Factory
        fields = ('country',)


class RetailNetworkFilter(CountryFilter):
    class Meta:
        model = RetailNetwork
        fields = ('country',)


class IndividualEntrepreneurFilter(CountryFilter):
    class Meta:
        model = IndividualEntrepreneur
        fields = ('country',)
