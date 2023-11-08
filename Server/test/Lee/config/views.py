from django.contrib.auth.models import User, Group
from django.http import HttpResponse, JsonResponse
from rest_framework import viewsets
from rest_framework import permissions
from rest_framework.decorators import api_view
import os
import requests
import json

import networkx as nx
# import osmnx as ox
import matplotlib.cm as cm
import matplotlib.colors as colors
import matplotlib as mpl
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
import folium
import geopandas as gpd

from .serializers import UserSerializer, GroupSerializer


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]



@api_view(['POST'])
def test_view(request):
    if request.method == 'POST':
        print(request)
        url = 'https://apis.openapi.sk.com/tmap/routes/pedestrian'
        appkey = 'AGDrqSCZzya3GshmeroNH8riWQSANOc868dvdL72'
        data = json.loads(request.body)
        print(data)

        # X, Y 좌표 바뀌어 있음
        startX = data['start']['start'][0]
        startY = data['start']['start'][1]
        endX = data['end']['end'][0]
        endY = data['end']['end'][1]
        startName = '출발지'
        endName = '도착지'
        print(startX, endX)

        header = {
            'Accept': 'application/json',
            'Content-Type' : 'application/json',
            'appKey' : 'AGDrqSCZzya3GshmeroNH8riWQSANOc868dvdL72'
        }
        data = {
            "startX": startY,
            "startY": startX,
            "endX": endY,
            "endY": endX,
            "startName": startName,
            "endName": endName
        }

        jsonData = requests.post(url, headers=header, json=data).json()

        print(jsonData)

        route_list = []

        for feature in jsonData['features']:
            types = feature['geometry']['type']

            if types == "LineString":
                values = feature['geometry']['coordinates']

                for value in values:
                    route_list.append(value)
        
        route_list2 = []
        for i, j in route_list:
            route_list2.append([i+0.001, j+0.001])

        print()
        print({"route": route_list, "route2": route_list2})
        print

        return JsonResponse({"route": route_list,"route2": route_list2}, status=200)
