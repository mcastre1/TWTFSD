from django.contrib.auth.models import User
from rest_framework import serializers

# Serializers
# Django uses an ORM


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        # Fields the serializer will take and return
        fields = ["id", "username", "password"]
        # We can pass in password when creating a new user, but not return it.
        extra_kwargs = {"password": {"write_only": True}}

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user
