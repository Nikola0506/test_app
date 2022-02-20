from django.urls import path

from .views import (
    DestinationListCustomersDetailsAPIView,
    DestinationCreateAPIView,
    DestinationChangeDataAPIView,
    DestinationDeleteAPIView,
    DestinationDetailsAPIView,
)

app_name = "destination"

urlpatterns = [
    path('destination-list/', DestinationListCustomersDetailsAPIView.as_view(), name='destination_list'),
    path('destination-create/', DestinationCreateAPIView.as_view(), name='destination_create'),
    path('destination-details/<int:id_destination>/', DestinationDetailsAPIView.as_view(), name='destination_details'),
    path('destination-change/<int:id_destination>/', DestinationChangeDataAPIView.as_view(), name='destination_change'),
    path('destination-delete/<int:id_destination>/', DestinationDeleteAPIView.as_view(), name='destination_delete')
]
