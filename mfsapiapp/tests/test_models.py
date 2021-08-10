from django.test import TestCase, Client
from ..models import Points
from ..serializers import PointsSerializer
from django.urls import reverse
import json
from rest_framework import status
class PointsTest(TestCase):
    """
    Test Models for Points Test Model
    """
    
    def setUp(self):
        Points.objects.create(name = "2", points_pair = [[3,3],[-2,4]], points = [[3, 3], [5, -1], [-2, 4]])
        Points.objects.create(name = "4", points_pair = [[4,6],[-3,4]], points = [[4, 6], [-3, 4], [200, 40]])

    def test_points_pair(self):
        pointed_pair = Points.objects.get(name = "2")
        self.assertEqual(pointed_pair.get_points(), 'The points [[3, 3], [5, -1], [-2, 4]]closest points[[3, 3], [-2, 4]] from 2')

class PointsViewTest(TestCase):
    """
    Test Views for Points Test Model
    """
    def setUp(self):
        # self.client = Client()
        # print(self.client)
        self.valid_payload = {
            "points": [[3, 3], [5, -1], [-2, 4]],
            "K": 2,
        }
        self.invalid_payload = {
            "points": [[3, 3], [5, -1], [-2, 4]]
        }

    def test_points_view(self):
        response = client.post(
            reverse('points'),
            data=json.dumps(self.valid_payload),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        
    def test_points_view_invalid_payload(self):
        response = client.post(
            reverse('points'),
            data=json.dumps(self.invalid_payload),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

# initialize the APIClient app
client = Client()