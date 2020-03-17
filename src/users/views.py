# from .forms import RegistrationForm
from rest_framework import status, generics, response, permissions
from .serializers import UsuarioRegistrationSerializer, UsuarioLoginSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from .models import Profile


class UserRegistrationView(generics.CreateAPIView):
    serializer_class = UsuarioRegistrationSerializer
    permission_classes = (permissions.AllowAny,)

    # @action(detail=False, methods=['post'])
    # def register(self, request):
    #     form = RegistrationForm(request.data)
    #     if form.is_valid():
    #         serializer = UsuarioSerializer(request.data)
    #         return Response(serializer.data, status=status.HTTP_201_CREATED)
    #     else:
    #         return Response(form.errors, status=status.HTTP_400_BAD_REQUEST)

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        response = {
            'success' : 'True',
            'status code' : status.HTTP_200_OK,
            'message': 'User registered  successfully',
            }
        status_code = status.HTTP_200_OK
        return response.Response(response, status=status_code)


class UserLoginView(TokenObtainPairView):
    serializer_class = UsuarioLoginSerializer
    permission_classes = (permissions.AllowAny,)

# class UserLoginView(generics.RetrieveAPIView):
#     permission_classes = (permissions.AllowAny,)
#     serializer_class = UsuarioLoginSerializer

#     def post(self, request):
#         serializer = self.serializer_class(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         response = {
#             'success' : 'True',
#             'status code' : status.HTTP_200_OK,
#             'message': 'User logged in  successfully',
#             'token' : serializer.data['token'],
#             }
#         status_code = status.HTTP_200_OK

#         return response.Response(response, status=status_code)


class ProfileView(generics.RetrieveAPIView):
    permission_classes = (permissions.IsAuthenticated,)

    def get(self, request):
        try:
            user_profile = Profile.objects.get(user=request.user)
            status_code = status.HTTP_200_OK
            response = {
                'success': 'true',
                'status code': status_code,
                'message': 'User profile fetched successfully',
                'data': [{
                    'first_name': user_profile.first_name,
                    'last_name': user_profile.last_name,
                    'phone_number': user_profile.phone_number,
                    'age': user_profile.age,
                    'gender': user_profile.gender,
                    }]
                }

        except Exception as e:
            status_code = status.HTTP_400_BAD_REQUEST
            response = {
                'success': 'false',
                'status code': status.HTTP_400_BAD_REQUEST,
                'message': 'User does not exists',
                'error': str(e)
                }
        return response.Response(response, status=status_code)