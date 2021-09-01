from django.contrib.auth import get_user_model
from model_controller.serializers import ModelControllerSerializer
from model_controller.utils import EXCLUDE_MODEL_CONTROLLER_FIELDS

from main.apps.authentication.serializers import UserSerializer
from main.apps.profiles.models import Profile


class ProfileSerializer(ModelControllerSerializer):
    """Serializer for Profile model"""
    user = UserSerializer()

    class Meta:
        model = Profile
        exclude = EXCLUDE_MODEL_CONTROLLER_FIELDS

    def create(self, validated_data):
        user_data = validated_data.pop('user')
        validated_data['user'] = get_user_model().objects.create_user(**user_data)
        return super().create(validated_data)
