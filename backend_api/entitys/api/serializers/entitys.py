# Import Third party
from rest_framework import serializers

# Import Model
from backend_api.entitys.models import Entity, TypeEntity


class TypeEntityModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = TypeEntity
        fields = '__all__'


class EntityModelSerializer(serializers.ModelSerializer):
    typeEntity = TypeEntityModelSerializer(read_only=True)

    class Meta:
        model = Entity
        fields = '__all__'


class EntityCreateModelSerializer(serializers.ModelSerializer):

    class Meta:
        model = Entity
        fields = '__all__'
