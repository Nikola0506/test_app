from django.contrib.auth import get_user_model
from rest_framework import serializers

UserCustome = get_user_model()


class CustomeUserSerializers(serializers.ModelSerializer):
    class Meta:
        model = UserCustome
        fields = (
            "id",
            "first_name",
            "last_name",
            "email",
            "username",
            "password",
            "is_superuser",
            "is_staff"
        )

        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        password = validated_data.pop('password', None)

        instance = self.Meta.model(**validated_data)
        if password is not None:
            instance.set_password(password)
        instance.save()
        return instance


class CustomeUserChangeSerializers(serializers.ModelSerializer):
    class Meta:
        model = UserCustome
        fields = (
            "id",
            "first_name",
            "last_name",
            "email",
            "username",
            "is_superuser",
            "is_staff"
        )
