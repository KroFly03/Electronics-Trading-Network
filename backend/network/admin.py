from django.contrib import admin

from network.models import Factory, Product, Contact, RetailNetwork, IndividualEntrepreneur

admin.site.register(Product)
admin.site.register(Contact)


class DefaultNetworkLinkAdmin(admin.ModelAdmin):
    list_display = ['name', 'contact', 'get_country', 'created']
    list_filter = ['contact__country']
    readonly_fields = ['created']

    def get_country(self, obj):
        return obj.contact.country

    get_country.short_description = 'Страна'


class DefaultNetworkLinkWithProviderAdmin(DefaultNetworkLinkAdmin):
    list_display = ['name', 'contact', 'get_provider', 'debt', 'get_country', 'created']
    fields = ['name', 'contact', 'product', 'debt', 'provider', 'created']
    readonly_fields = ['created', 'provider']
    actions = ['clear_debt']

    def get_provider(self, obj):
        return obj.provider.name

    get_provider.short_description = 'Поставщик'

    def clear_debt(self, request, queryset):
        queryset.update(debt=0.00)

    clear_debt.short_description = 'Аннулировать задолжность'


@admin.register(Factory)
class FactoryAdmin(DefaultNetworkLinkAdmin):
    pass


@admin.register(RetailNetwork)
class RetailNetworkAdmin(DefaultNetworkLinkWithProviderAdmin):
    pass


@admin.register(IndividualEntrepreneur)
class IndividualEntrepreneurAdmin(DefaultNetworkLinkWithProviderAdmin):
    pass
