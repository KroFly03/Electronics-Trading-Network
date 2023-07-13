from rest_framework import serializers

from network.models import Factory, IndividualEntrepreneur, RetailNetwork, Contact, Product


class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = '__all__'


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'


class FactoryCreateUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Factory
        fields = '__all__'
        read_only_fields = ('id', 'created')


class FactorySerializer(serializers.ModelSerializer):
    contact = ContactSerializer(read_only=True)
    product = ProductSerializer(many=True, read_only=True)

    class Meta:
        model = Factory
        fields = '__all__'
        read_only_fields = ('id', 'created')


class ProviderSerializer(serializers.ModelSerializer):
    contact = ContactSerializer(read_only=True)
    product = ProductSerializer(many=True, read_only=True)
    provider = serializers.CharField(source='provider.name', read_only=True)


class RetailNetworkCreateSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        read_only_fields = ('id', 'created')
        model = RetailNetwork


class RetailNetworkUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        read_only_fields = ('id', 'created', 'debt')
        model = RetailNetwork


class RetailNetworkSerializer(ProviderSerializer):
    class Meta:
        fields = '__all__'
        read_only_fields = ('id', 'created')
        model = RetailNetwork


class IndividualEntrepreneurCreateSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        read_only_fields = ('id', 'created')
        model = IndividualEntrepreneur


class IndividualEntrepreneurUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        read_only_fields = ('id', 'created', 'debt')
        model = IndividualEntrepreneur


class IndividualEntrepreneurSerializer(ProviderSerializer):
    class Meta:
        fields = '__all__'
        read_only_fields = ('id', 'created')
        model = IndividualEntrepreneur
