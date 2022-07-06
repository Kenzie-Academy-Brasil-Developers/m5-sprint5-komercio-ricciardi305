from rest_framework import serializers
from .models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "email", "password", "first_name", "last_name", "is_seller", "date_joined"]
        extra_kwargs = {"password": {"write_only": True}}

    def create(self, validated_data):
        user = User(**validated_data)
        user.set_password(validated_data['password'])
        user.save()
        return user


class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField()

class IsActiveSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "email", "password", "first_name", "last_name", "is_seller", "date_joined", "is_active"]
        read_only_fields = ["id", "email", "password", "first_name", "last_name", "is_seller", "date_joined"]

