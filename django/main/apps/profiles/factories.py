import factory

from main.apps.common.factories import ModelControllerFactory
from main.apps.profiles.models import Profile


class ProfileFactory(ModelControllerFactory):
    class Meta:
        model = Profile

    user = factory.SubFactory('main.apps.authentication.factories.UserFactory')
