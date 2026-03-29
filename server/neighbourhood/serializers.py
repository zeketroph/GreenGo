from rest_framework import serializers
from .models import NeighbourhoodData, CommunityMember, FlowerInNeighbourhood

class NeighbourhoodDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = NeighbourhoodData
        fields = '__all__'

class CommunityMemberSerializer(serializers.ModelSerializer):
    class Meta:
        model = CommunityMember
        fields = '__all__'

class FlowerInNeighbourhoodSerializer(serializers.ModelSerializer):
    class Meta:
        model = FlowerInNeighbourhood
        fields = '__all__'