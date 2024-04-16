from rest_framework import serializers
from .models import Cities, Tours, TourLength
import datetime


class CitySerializer(serializers.Serializer):
    class Meta:
        model = Cities
        fields = ['tour_city']


class DateStart(serializers.Serializer):
    day_start = serializers.DateField(initial=datetime.date.today)


class DateEnd(serializers.Serializer):
    day_end = serializers.DateField(initial=datetime.date.today)


class LengthSerializer(serializers.Serializer):
    class Meta:
        model = TourLength
        fields = ['length']


class TourSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tours
        fields = "__all__"