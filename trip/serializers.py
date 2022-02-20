from rest_framework import serializers

from destination.models import Destination
from trip.models import Trip


class TripSerializers(serializers.ModelSerializer):
    class Meta:
        model = Trip
        fields = '__all__'


class HotelSerializers(serializers.ModelSerializer):
    class Meta:
        model = Destination
        fields = ('hotel',)
