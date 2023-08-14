from django.db.models import Sum
from rest_framework import viewsets, status
from rest_framework.response import Response
from .models import EnergyMeter, EnergyMeasurements
from .serializers import EnergyMeterSerializer


class EnergyMeterViewSet(viewsets.ViewSet):
    def create(self, request):
        serializer = EnergyMeterSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk=None):
        try:
            energy_meter = EnergyMeter.objects.get(pk=pk)
            energy_meter.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except EnergyMeter.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def retrieve(self, request, pk=None):
        try:
            energy_meter = EnergyMeter.objects.get(pk=pk)
            current_measurement = EnergyMeasurements.objects.filter(
                number=energy_meter.number
            ).first()
            total_kilowatt = EnergyMeasurements.objects.filter(
                number=energy_meter.number
            ).aggregate(total_kilowatt=Sum('kilowatt'))['total_kilowatt']

            response_data = {
                'number': energy_meter.number,
                'amps': current_measurement.amps if current_measurement else None,
                'kilowatt': total_kilowatt if total_kilowatt else 0,
            }

            return Response(response_data)
        except EnergyMeter.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
