from rest_framework import serializers
from .models import Line, Station


class LineSerializer(serializers.ModelSerializer):
    stations = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    class Meta:
        model = Line
        fields = ('name', 'stations')


class StationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Station
        fields = ('name', 'lines')
