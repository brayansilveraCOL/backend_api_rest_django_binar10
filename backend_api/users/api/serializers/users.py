# Import Serializer
from django.contrib.auth import password_validation
from rest_framework.validators import UniqueValidator
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework import serializers

# Import python
from datetime import datetime

# Import Models
from backend_api.users.models import User
from backend_api.entitys.models import Entity
from backend_api.locations.models import Country


class LoginSerializer(TokenObtainPairSerializer):
    """
        Class obtain Token
    """

    def validate(self, attrs):
        """
        overwrite validate Function to add more fields
        :param attrs:
        :return: data
        """
        data = super().validate(attrs)
        refresh = self.get_token(self.user)
        data['refresh'] = str(refresh)
        data['access'] = str(refresh.access_token)
        data['username'] = self.user.username
        data['email'] = self.user.email
        data['date'] = datetime.now()

        return data


class UserModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


class UserEditModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'
        read_only_fields = (
            'email',
            'identify',
        )


class UserSignUpSerializer(serializers.Serializer):
    email = serializers.EmailField(
        validators=[UniqueValidator(queryset=User.objects.all())]
    )
    username = serializers.CharField(
        min_length=4,
        max_length=20,
        validators=[UniqueValidator(queryset=User.objects.all())]
    )
    # identify
    identify = serializers.CharField(
        min_length=4,
        max_length=20,
        validators=[UniqueValidator(queryset=User.objects.all())]
    )

    # Name
    first_name = serializers.CharField(min_length=2, max_length=30)
    last_name = serializers.CharField(min_length=2, max_length=30)

    # ForeignKey
    entity = serializers.PrimaryKeyRelatedField(queryset=Entity.objects.filter(state=True))
    country = serializers.PrimaryKeyRelatedField(queryset=Country.objects.filter(state=True))

    # Password
    password = serializers.CharField(min_length=8, max_length=64)
    password_confirmation = serializers.CharField(min_length=8, max_length=64)

    def validate(self, data):
        """Verify passwords match."""
        passwd = data['password']
        passwd_conf = data['password_confirmation']
        if passwd != passwd_conf:
            raise serializers.ValidationError("Passwords don't match.")
        password_validation.validate_password(passwd)
        return data

    def create(self, validated_data):
        data = validated_data
        data.pop('password_confirmation')
        print(data)
        user = User.objects.create_user(**data)
        user.save()
        return user
