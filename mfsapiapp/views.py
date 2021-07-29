from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser

# Create your views here.
@csrf_exempt
def pClosest(request):
    # points, K
    # print("show points", points)
    # print("Show k", K)
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
    
    
# points = [[3, 3], [5, -1], [-2, 4]]
# points = [(2,3), (1,1), (5, 4)]
 
# K = 2

# request.method == 'POST'

# print(pClosest(request, points, K))

