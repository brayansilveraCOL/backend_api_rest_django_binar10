# Django
from django.urls import include, path

# Django REST Framework
from rest_framework.routers import DefaultRouter

# Views
from backend_api.entitys.api.views.entitys import EntityViewSet, TypeEntityViewSet


router = DefaultRouter()
router.register(r'entity', EntityViewSet, basename='entity'),
router.register(r'typeEntity', TypeEntityViewSet, basename='typeEntity'),




urlpatterns = [
    path('', include(router.urls))
]