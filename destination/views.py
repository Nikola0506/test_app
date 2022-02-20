from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from .models import Destination
from .serializers import DestinationSerializers


# Create your views here.

class DestinationDetailsAPIView(generics.RetrieveAPIView):
    permission_classes = [IsAuthenticated, ]
    lookup_field = 'id_destination'
    queryset = Destination.objects.all().order_by('id_destination')
    serializer_class = DestinationSerializers


class DestinationListCustomersDetailsAPIView(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated, ]
    queryset = Destination.objects.all().order_by('id_destination')
    serializer_class = DestinationSerializers


class DestinationCreateAPIView(generics.CreateAPIView):
    permission_classes = [IsAuthenticated, ]
    queryset = Destination.objects.all().order_by('id_destination')
    serializer_class = DestinationSerializers


class DestinationChangeDataAPIView(generics.RetrieveUpdateAPIView):
    permission_classes = [IsAuthenticated, ]
    lookup_field = 'id_destination'
    queryset = Destination.objects.all().order_by('id_destination')
    serializer_class = DestinationSerializers


class DestinationDeleteAPIView(generics.RetrieveDestroyAPIView):
    permission_classes = [IsAuthenticated, ]
    lookup_field = 'id_destination'
    queryset = Destination.objects.all().order_by('id_destination')
    serializer_class = DestinationSerializers
