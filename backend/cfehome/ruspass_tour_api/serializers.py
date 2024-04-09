from rest_framework import serializers
from .models import Cities, Tours


class CitySerializer(serializers.Serializer):
    class Meta:
        model = Cities
        fields = ['tour_city']
