from rest_framework import serializers

from .models import Car

class CarsSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('id', 'car_type', 'car_disc', 'driver', 'created_at')
        model = Car