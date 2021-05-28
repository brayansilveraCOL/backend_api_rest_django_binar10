from backend_api.users.api.serializers.users import LoginSerializer
from rest_framework_simplejwt.views import TokenObtainPairView

# Import Models
from backend_api.users.models import User

# Import Serializers
from backend_api.users.api.serializers.users import UserModelSerializer, UserEditModelSerializer, UserSignUpSerializer

# Django REST Framework
from rest_framework import mixins, status, viewsets
from rest_framework.decorators import action
from rest_framework.exceptions import ParseError
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.filters import SearchFilter


class LoginView(TokenObtainPairView):
    """
    Create View with Serializer Class
    """
    serializer_class = LoginSerializer


class UserViewSet(
    mixins.UpdateModelMixin,
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    viewsets.GenericViewSet,
):
    """
        ViewSet Manage Request User
    """

    queryset = User.objects.filter(is_active=True)
    serializer_class = UserModelSerializer
    lookup_field = 'uniqueCode'

    filter_backends = [SearchFilter]
    search_fields = ['email', 'identify', 'first_name', 'last_name']

    def get_permissions(self):
        """Assign permissions based on action."""
        permissions = [IsAuthenticated]
        return [permission() for permission in permissions]

    @action(detail=True, methods=['PATCH'])
    def upload(self, request, *args, **kwargs):
        """Upload Image."""
        user = self.get_object()
        if user.email == request.user.email:
            try:
                image = request.data['image']
            except KeyError:
                raise ParseError('Request has no resource file attached')
            user_upload = User.objects.filter(id=user.pk).first()
            user_upload.image = image
            user_upload.save()
            data = {
                'msg': 'Image Upload'
            }
            return Response(data=data, status=status.HTTP_201_CREATED)
        else:
            return Response(status=status.HTTP_401_UNAUTHORIZED)

    def update(self, request, *args, **kwargs):
        """
        validate Request User
        :param request:
        :param args:
        :param kwargs:
        :return:
        """
        if request:
            user = self.get_object()
            if user.email == request.user.email:
                if user:
                    serializer = UserEditModelSerializer(user, request.data, partial=True)
                    serializer.is_valid(raise_exception=True)
                    serializer.save()
                    return Response(serializer.data, status=status.HTTP_200_OK)
                else:
                    return Response(status=status.HTTP_400_BAD_REQUEST)

            else:
                return Response(status=status.HTTP_401_UNAUTHORIZED)

        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, *args, **kwargs):
        """
        Return Detail User
        :param request:
        :param args:
        :param kwargs:
        :return: Response object
        """
        response = super(UserViewSet, self).retrieve(request, *args, **kwargs)
        data = response.data
        data.pop('password')
        data.pop('groups')
        data.pop('user_permissions')
        return Response(data=data, status=status.HTTP_200_OK)


class UserSignupView(mixins.CreateModelMixin,
                     viewsets.GenericViewSet):
    """
    Class Signup to Create User
    """

    def create(self, request, *args, **kwargs):
        """
        function create to User
        :param request:
        :param args:
        :param kwargs:
        :return: Response Object
        """
        if request:
            serializer = UserSignUpSerializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            user = serializer.save()
            data = UserModelSerializer(user).data
            return Response(data, status=status.HTTP_201_CREATED)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)
