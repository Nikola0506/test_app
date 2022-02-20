# Create your views here.
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics, filters
from rest_framework.permissions import IsAuthenticated
from rest_framework.settings import api_settings

from custome_user.serializers import CustomeUserSerializers, CustomeUserChangeSerializers
from .models import CustomeUsers


class CustomerUserListAPIview(generics.ListAPIView):
    """user list"""
    permission_classes = [IsAuthenticated, ]
    queryset = CustomeUsers.objects.all().order_by('id')
    serializer_class = CustomeUserSerializers
    pagination_class = None

    filter_backends = api_settings.DEFAULT_FILTER_BACKENDS + [
        filters.OrderingFilter,
        DjangoFilterBackend,
    ]
    filterset_fields = {
        "username": ["exact"],
    }


class CustomeUserDetailsAPIview(generics.RetrieveAPIView):
    """get user by id - details"""
    permission_classes = [IsAuthenticated, ]
    lookup_field = 'id'
    queryset = CustomeUsers.objects.all().order_by('id')
    serializer_class = CustomeUserSerializers


class CustomeUserCreateAPIview(generics.CreateAPIView):
    permission_classes = [IsAuthenticated, ]
    """create user"""
    queryset = CustomeUsers.objects.all().order_by('id')
    serializer_class = CustomeUserSerializers


class CustomeUserChangeAPIview(generics.RetrieveUpdateAPIView):
    permission_classes = [IsAuthenticated, ]
    """customize user"""
    lookup_field = 'id'
    queryset = CustomeUsers.objects.all().order_by('id')
    serializer_class = CustomeUserChangeSerializers


class CustomeuserDeleteAPIview(generics.RetrieveDestroyAPIView):
    permission_classes = [IsAuthenticated, ]
    """delete user"""
    lookup_field = 'id'
    queryset = CustomeUsers.objects.all().order_by('id')
    serializer_class = CustomeUserSerializers
