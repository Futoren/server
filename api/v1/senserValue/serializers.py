from rest_framework import serializers
from sensor.models import Sensor


class SensorSerializer(serializers.ModelSerializer):
    created_at = serializers.DateTimeField(read_only=True)

    class Meta:
        model = Sensor
        fields = ['id', 'DeviceName', 'Action', 'SensorName', 'x', 'y', 'z', 'created_at']
