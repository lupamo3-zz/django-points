from rest_framework import serializers
from mfsapiapp.models import Points


class PointsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Points
        fields = ('name', 'points', 'points_pair')

    name = serializers.CharField(max_length=100)
    points = serializers.ListField()
    points_pair = serializers.ListField()

    def create(self, validated_data):
        """
        Create  a new  instance  of  the  model  based  on  the  validated  data.
        """
        return Points.objects.create(**validated_data)


