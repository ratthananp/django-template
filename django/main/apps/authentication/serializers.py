from django.contrib.auth import get_user_model
from rest_framework import serializers, validators
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer


class UserSerializer(serializers.ModelSerializer):
    """Serializer for User model"""
    class Meta:
        model = get_user_model()
        fields = ('username', 'password', 'email', 'first_name', 'last_name')
        extra_kwargs = {
            'username': {
                'validators': [
                    validators.UniqueValidator(queryset=get_user_model().objects.all())
                ]
            },
            'email': {
                'validators': [
                    validators.UniqueValidator(queryset=get_user_model().objects.all())
                ]
            },
            'password': {
                'read_only': True
            }
        }


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    """Serializer for returning JWT token"""
    def validate(self, attrs):
        data = super().validate(attrs)

        refresh = self.get_token(self.user)

        data['refresh'] = str(refresh)
        data['access'] = str(refresh.access_token)

        # add extra responses
        data['user'] = UserSerializer(self.user).data
        data['role'] = str(self.user.profile.role)

        return data
