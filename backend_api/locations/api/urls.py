# Django
from django.urls import include, path

# Django REST Framework
from rest_framework.routers import DefaultRouter

# Views
from backend_api.locations.api.views.locations import CountryViewSet

router = DefaultRouter()
router.register(r'country', CountryViewSet, basename='country'),

urlpatterns = [
    path('', include(router.urls))
]
