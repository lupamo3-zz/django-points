from django.test import TestCase
from ..models import Points

class PointsTest(TestCase):
    """
    Test Models for Points Test Model
    """
    

    def create_points_pair(self):
        Points.objects.create(name = "2", points_pair = [[3,3],[-2,4]], points = [[3, 3], [5, -1], [-2, 4]])
        Points.objects.create(name = "4", points_pair = [[4,6],[-3,4]], points = [[4, 6], [-3, 4], [200, 40]])