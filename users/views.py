import json
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.authtoken.models import Token
from rest_framework.authentication import TokenAuthentication
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from django.core.exceptions import ValidationError
from django.contrib.auth.hashers import check_password
from users.permissions import UserApiPermissions

from users.serializers import UserRegistraionSerializer, UserSerializer
from users.models import User

class UserRegisterAPIView(APIView):
    """
    View to register a new user
    """
    permission_classes = [AllowAny]
    
    def post(self, request, *args, **kwargs):
        """
        api to create token and register a new user
        """
        serializer = UserRegistraionSerializer(data=request.data)
        data = {}

        if serializer.is_valid(raise_exception=True):
            user = serializer.save()
            token = Token.objects.get_or_create(user=user)[0].key
            user.set_password(serializer.data['password'])
            user.save()
            data['token'] = token
            data['message'] = "Account created successfully"
        else:
            raise ValidationError(serializer.errors)
        
        return Response(data)


class LoginAPIView(APIView):
    """
    User Login api
    """
    permission_classes = [AllowAny]
    model = User

    def post(self, request, *args, **kwargs):
        """
        login api
        """
        creds = json.loads(request.body)
        email = creds['email']
        password = creds['password']

        # trying to find a user with given email and password
        try:
            Account = User.objects.get(email=email)
        except BaseException as e:
            raise ValidationError("Invalid creds", status_code=400)
        
        if not check_password(password, Account.password):
            raise ValidationError({"message": "Incorrect Login credentials"})
        
        token = Token.objects.get_or_create(user=Account)[0].key

        if Account and Account.is_active:
            data = {
                "token": token,
                "username": Account.user_name,
                "email": email,
            }
            return Response(data)

   
class LogoutAPIView(APIView):
    """
    User Logout api
    """
    permission_classes = [IsAuthenticated]
    authentication_classes = [TokenAuthentication]

    def post(self, request, *args, **kwargs):
        request.user.auth_token.delete()
        return Response("Logged out Successfully")

class UserViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (IsAuthenticated,)
    http_method_names = ['get', 'patch' ]
    lookup_field = "pk"


