from rest_framework import serializers

from .models import Sensor, Measurement


# TODO: опишите необходимые сериализаторы

class SensorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sensor
        fields = '__all__'


class MeasurementPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Measurement
        fields = [
            'sensor',
            'temperature',
        ]


class MeasurementGetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Measurement
        fields = [
            'temperature',
            'created_at'
        ]


class SensorMeasurementSerializer(serializers.ModelSerializer):
    measurements = MeasurementGetSerializer(many=True, read_only=True)

    class Meta:
        model = Sensor
        fields = ['id', 'name', 'description', 'measurements']
