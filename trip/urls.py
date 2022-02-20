from django.urls import path

from .views import (
    TripListCustomersDetailsAPIView,
    TripCreateAPIView,
    TripChangeDataAPIView,
    TripDeleteAPIView,
    TripDetailsAPIView,
)

app_name = "trip"

urlpatterns = [
    path('', TripListCustomersDetailsAPIView.as_view(), name='trip_list'),
    path('trip-create/', TripCreateAPIView.as_view(), name='trip_create'),
    path('trip-details/<int:id_trip>/', TripDetailsAPIView.as_view(), name='trip_details'),
    path('trip-change/<int:id_trip>/', TripChangeDataAPIView.as_view(), name='trip_change'),
    path('trip-delete/<int:id_trip>/', TripDeleteAPIView.as_view(), name='trip_delete')
]
