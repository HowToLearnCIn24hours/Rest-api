from rest_framework import serializers
from .models import Cities, Tours, TourLength
import datetime


class CitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Cities
        fields = ['tour_city']


class DateStart(serializers.Serializer):
    day_start = serializers.DateField(initial=datetime.date.today)


class DateEnd(serializers.Serializer):
    day_end = serializers.DateField(initial=datetime.date.today)


class LengthSerializer(serializers.ModelSerializer):
    class Meta:
        model = TourLength
        fields = ['length']

    def correct_length(self, value):
        """
        Check that length is a positive number.
        """
        if value['length'] <= '0':
            raise serializers.ValidationError("Введите продолжительность больше 0 дней")
        return value


class TourSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tours
        fields = "__all__"