from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from rest_framework.decorators import api_view

from .serializers import PointsSerializer
from .models import Points

# Create your views here.
@api_view(['GET', 'POST'])
@csrf_exempt
def pClosest(request):
    """
    Function to get closest points,
    points: list of points
    K: number of points to return
    pClosest: list of 2 closest points
    """
    
    # get the number of points  
    if request.method == 'POST':
        data = JSONParser().parse(request)
        points = data['points']
        K = data['K']

        points.sort(key = lambda K: K[0]**2 + K[1]**2)
    
        return HttpResponse(points[:K], content_type='json')
    
    elif request.method == 'GET':
        return JsonResponse(points, safe=False)
