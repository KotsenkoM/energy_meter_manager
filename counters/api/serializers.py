from rest_framework import serializers

from .models import EnergyMeter, EnergyMeasurements


class EnergyMeasurementsSerializer(serializers.ModelSerializer):

    class Meta:
        model = EnergyMeasurements
        fields = '__all__'


class EnergyMeterSerializer(serializers.ModelSerializer):

    class Meta:
        model = EnergyMeter
        fields = '__all__'
