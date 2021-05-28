# Import Serializer
from backend_api.entitys.api.serializers.entitys import EntityCreateModelSerializer, TypeEntityModelSerializer

# Import Models
from backend_api.entitys.models import Entity, TypeEntity

# Import Third Party Library
from rest_framework import mixins
from rest_framework.viewsets import GenericViewSet
from rest_framework.permissions import IsAuthenticated


class EntityViewSet(mixins.ListModelMixin,
                    mixins.RetrieveModelMixin,
                    mixins.UpdateModelMixin,
                    mixins.DestroyModelMixin,
                    mixins.CreateModelMixin,
                    GenericViewSet):
    serializer_class = EntityCreateModelSerializer
    queryset = Entity.objects.filter(state=True)
    lookup_field = 'uniqueCode'

    def get_permissions(self):
        """Assign permissions based on action."""
        permissions = [IsAuthenticated]
        return [permission() for permission in permissions]

    def perform_destroy(self, instance):
        """Disable Entity."""
        instance.state = False
        instance.save()


class TypeEntityViewSet(mixins.ListModelMixin,
                        mixins.RetrieveModelMixin,
                        mixins.UpdateModelMixin,
                        mixins.DestroyModelMixin,
                        mixins.CreateModelMixin,
                        GenericViewSet):
    serializer_class = TypeEntityModelSerializer
    queryset = TypeEntity.objects.filter(state=True)
    lookup_field = 'uniqueCode'

    def get_permissions(self):
        """Assign permissions based on action."""
        permissions = [IsAuthenticated]
        return [permission() for permission in permissions]

    def perform_destroy(self, instance):
        """Disable Entity."""
        instance.state = False
        instance.save()
