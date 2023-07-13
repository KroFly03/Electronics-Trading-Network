from django.urls import path

from network.views import factory, retail_network, individual_entrepreneur

urlpatterns = [
    # Factory

    path('factories/create', factory.FactoryCreateView.as_view(), name='create_factory'),
    path('factories/list', factory.FactoryListView.as_view(), name='list_factory'),
    path('factories/<int:pk>', factory.FactoryDetailDeleteView.as_view(), name='detail_factory'),
    path('factories/<int:pk>/update', factory.FactoryUpdateView.as_view(), name='update_factory'),
    path('factories/<int:pk>/delete', factory.FactoryDetailDeleteView.as_view(), name='delete_factory'),

    # RetailNetwork

    path('retails/create', retail_network.RetailNetworkCreateView.as_view(), name='create_retail'),
    path('retails/list', retail_network.RetailNetworkListView.as_view(), name='list_retail'),
    path('retails/<int:pk>', retail_network.RetailNetworkDetailDeleteView.as_view(), name='detail_retail'),
    path('retails/<int:pk>/update', retail_network.RetailNetworkUpdateView.as_view(), name='update_retail'),
    path('retails/<int:pk>/delete', retail_network.RetailNetworkDetailDeleteView.as_view(), name='delete_retail'),

    # IndividualEntrepreneur

    path('ies/create', individual_entrepreneur.IndividualEntrepreneurCreateView.as_view(), name='create_ie'),
    path('ies/list', individual_entrepreneur.IndividualEntrepreneurListView.as_view(), name='list_ie'),
    path('ies/<int:pk>', individual_entrepreneur.IndividualEntrepreneurDetailDeleteView.as_view(),
         name='detail_ie'),
    path('ies/<int:pk>/update', individual_entrepreneur.IndividualEntrepreneurUpdateView.as_view(),
         name='update_ie'),
    path('ies/<int:pk>/delete', individual_entrepreneur.IndividualEntrepreneurDetailDeleteView.as_view(),
         name='delete_ie'),
]
