from rest_framework import serializers
from .models import Usuario
from mrp.models import BomFile, MastFile, InvFile, ItemMasterFile
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer


class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = ['first_name', 'last_name', 'email']


class UsuarioRegistrationSerializer(serializers.ModelSerializer):

    class Meta:
        model = Usuario
        fields = ['email', 'password', 'first_name', 'last_name']
        extra_kwargs = {'password': {'write_only': True}}

        def create(self, validated_data):
            user = UsuarioSerializer({
                'email': validated_data['email'],
                'password': validated_data['password'],
                'first_name': validated_data['first_name'],
                'last_name': validated_data['last_name']
            })
            return user



class UsuarioLoginSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        # Add custom claims
        token['name'] = user.email
        # ...

        return token