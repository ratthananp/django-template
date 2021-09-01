from django.urls import path
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenRefreshView

from main.apps.authentication.views import MyTokenObtainPairView
from main.apps.profiles.views import ProfileViewSet

router = DefaultRouter()
app_name = 'api_urls'

# Register your API router here. It should be sorted by alphabet.
router.register('profiles', ProfileViewSet)

urlpatterns = [
    path('token-auth/', MyTokenObtainPairView.as_view(), name='token-auth'),
    path('token-refresh/', TokenRefreshView.as_view(), name='token-refresh')
]

urlpatterns += router.urls
