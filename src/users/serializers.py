from django.contrib.auth import authenticate
from django.contrib.auth.models import update_last_login
from rest_framework import serializers
from .models import Usuario, Profile
from mrp.models import BomFile, MastFile, InvFile, ItemMasterFile
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

class UsuarioSerializer(serializers.ModelSerializer):
    bom_files = serializers.PrimaryKeyRelatedField( required=False,
        many=True, queryset=BomFile.objects.all())

    mast_files = serializers.PrimaryKeyRelatedField( required=False,
        many=True, queryset=MastFile.objects.all())

    inv_files = serializers.PrimaryKeyRelatedField( required=False,
        many=True, queryset=InvFile.objects.all())

    item_master_files = serializers.PrimaryKeyRelatedField( required=False,
        many=True, queryset=ItemMasterFile.objects.all())

    class Meta:
        model = Profile
        fields = ['first_name', 'last_name', 'gender', 'bom_files',
            'mast_files', 'inv_files', 'item_master_files']


class UsuarioRegistrationSerializer(serializers.ModelSerializer):
    profile = UsuarioSerializer(required=False)

    class Meta:
        model = Usuario
        fields = ['email', 'password', 'profile']
        extra_kwargs = {'password': {'write_only': True}}

        def create(self, validated_data):
            profile_data = validated_data.pop('profile')
            user = Usuario.objects.create_user(**validated_data)
            Profile.objects.create(
                user=user,
                first_name=profile_data['first_name'],
                last_name=profile_data['last_name'],
                gender=profile_data['gender']
            )
            return user

class UsuarioLoginSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        # Add custom claims
        token['name'] = user.email
        # ...

        return token


# class UsuarioLoginSerializer(serializers.Serializer):
#     email = serializers.CharField(max_length=255)
#     password = serializers.CharField(max_length=128, write_only=True)
#     token = serializers.CharField(max_length=255, read_only=True)

#     def validate(self, data):
#         email = data.get("email", None)
#         password = data.get("password", None)
#         user = authenticate(email=email, password=password)
#         if user is None:
#             raise serializers.ValidationError(
#                 'A user with this email and password is not found.'
#             )
#         try:
#             payload = JWT_PAYLOAD_HANDLER(user)
#             jwt_token = JWT_ENCODE_HANDLER(payload)
#             update_last_login(None, user)
#         except Usuario.DoesNotExist:
#             raise serializers.ValidationError(
#                 'User with given email and password does not exists'
#             )
#         return {
#             'email':user.email,
#             'token': jwt_token
#         }