from rest_framework import serializers
from .models import FlowerData

class FlowerDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = FlowerData
        fields = '__all__'