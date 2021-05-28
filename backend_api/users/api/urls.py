from django.urls import path, include
# Third apps imports
from rest_framework_simplejwt.views import (
    TokenRefreshView,
)
from backend_api.users.api.views.users import LoginView

from rest_framework.routers import DefaultRouter

# views
from backend_api.users.api.views.users import UserViewSet, UserSignupView

router = DefaultRouter()
router.register(r'user', UserViewSet, basename='user')
router.register(r'signup', UserSignupView, basename='user-signup')


urlpatterns = [
    path('', include(router.urls)),
    path('login/', LoginView.as_view(), name='token_obtain'),
    path('refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]