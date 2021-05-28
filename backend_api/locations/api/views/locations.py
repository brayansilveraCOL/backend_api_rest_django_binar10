# Import Serializer
from backend_api.locations.api.serializers.locations import CountryModelSerializer

# Import Models
from backend_api.locations.models import Country

# Import Third Party Library
from rest_framework import mixins
from rest_framework.viewsets import GenericViewSet
from rest_framework.permissions import IsAuthenticated


class CountryViewSet(mixins.ListModelMixin,
                     mixins.RetrieveModelMixin,
                     mixins.UpdateModelMixin,
                     mixins.DestroyModelMixin,
                     mixins.CreateModelMixin,
                     GenericViewSet):
    serializer_class = CountryModelSerializer
    queryset = Country.objects.filter(state=True)
    lookup_field = 'uniqueCode'

    def get_permissions(self):
        """Assign permissions based on action."""
        permissions = [IsAuthenticated]
        return [permission() for permission in permissions]

    def perform_destroy(self, instance):
        """Disable Country."""
        instance.state = False
        instance.save()
