from rest_framework_simplejwt.views import TokenObtainPairView

from main.apps.authentication.serializers import MyTokenObtainPairSerializer


class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer
