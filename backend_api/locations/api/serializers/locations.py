# Import Third party
from rest_framework import serializers

# Import Model
from backend_api.locations.models import Country


class CountryModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields = '__all__'
