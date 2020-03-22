from rest_framework import status, generics, response, permissions, viewsets
from .models import Usuario
from rest_framework.response import Response
from .serializers import UsuarioRegistrationSerializer, UsuarioLoginSerializer, UsuarioSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken
from .forms import RegistrationForm
from rest_framework.authentication import SessionAuthentication, BasicAuthentication

class UserViewSet(viewsets.ModelViewSet):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer
    permission_classes = [permissions.IsAdminUser]

class UserProfileView(generics.RetrieveAPIView):

    def get(self, request):
        try:
            user_profile = Usuario.objects.get(pk=request.user.pk)
            status_code = status.HTTP_200_OK
            response = {
                    'first_name': user_profile.first_name,
                    'last_name': user_profile.last_name,
                    'gender': user_profile.gender
                }

        except Exception as e:
            status_code = status.HTTP_400_BAD_REQUEST
            response = {
                'success': 'false',
                'status code': status.HTTP_400_BAD_REQUEST,
                'message': 'User does not exists',
                'error': str(e)
                }
        return Response(response, status=status_code)


class UserRegistrationView(APIView):
    permission_classes = (permissions.AllowAny,)

    def post(self, request):
        form = RegistrationForm(request.data)
        if form.is_valid():
            form.save()
            status_code = status.HTTP_201_CREATED
            response = {
                'success' : 'True',
                'status code' : status_code,
                'message': 'User registered  successfully',
            }
            return Response(response, status=status_code)
        else:
            return Response(form.errors, status=status.HTTP_400_BAD_REQUEST)

class UserLoginView(TokenObtainPairView):
    permission_classes = (permissions.AllowAny,)
    serializer_class = UsuarioLoginSerializer

class LogoutAndBlacklistRefreshTokenForUserView(APIView):
    def post(self, request):
        try:
            print("\n\n\n-------------------")
            print(request.data)
            refresh_token = request.data["refresh_token"]
            token = RefreshToken(refresh_token)
            print(token)
            token.blacklist()
            print("line 76")
            return Response(status=status.HTTP_205_RESET_CONTENT)
        except Exception as e:
            return Response(status=status.HTTP_400_BAD_REQUEST)