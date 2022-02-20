from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from .models import Trip
from .serializers import TripSerializers


# Create your views here.

class TripDetailsAPIView(generics.RetrieveAPIView):
    permission_classes = [IsAuthenticated, ]
    lookup_field = 'id_trip'
    queryset = Trip.objects.all().order_by('id_trip')
    serializer_class = TripSerializers


class TripListCustomersDetailsAPIView(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated, ]
    queryset = Trip.objects.all().order_by('id_trip')
    serializer_class = TripSerializers


class TripCreateAPIView(generics.CreateAPIView):
    permission_classes = [IsAuthenticated, ]
    queryset = Trip.objects.all().order_by('id_trip')
    serializer_class = TripSerializers


class TripChangeDataAPIView(generics.RetrieveUpdateAPIView):
    permission_classes = [IsAuthenticated, ]
    lookup_field = 'id_trip'
    queryset = Trip.objects.all().order_by('id_trip')
    serializer_class = TripSerializers


class TripDeleteAPIView(generics.RetrieveDestroyAPIView):
    permission_classes = [IsAuthenticated, ]
    lookup_field = 'id_trip'
    queryset = Trip.objects.all().order_by('id_trip')
    serializer_class = TripSerializers
