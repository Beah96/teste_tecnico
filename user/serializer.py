from rest_framework import serializers
from .models import User

class UserSerializer (serializers.ModelSerializer):
    class Meta:
        model: User
        fields = ['id', 'username', 'password', 'email', 'is_superuser']

    def create(self, validated_data : dict) -> User:
        if validated_data['is_superuser'] == True:
            instance = User.objects.create_superuser(**validated_data)
        else:
            instance = User.objects.create_user(**validated_data)
        return instance