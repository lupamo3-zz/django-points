from rest_framework import serializers
from mfsapiapp.models import Points


class PointsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Points
        fields = ('name', 'points', 'points_pair')

    name = serializers.CharField(max_length=100)
    points = serializers.CharField(max_length=100)
    points_pair = serializers.CharField(max_length=100)


