from django.shortcuts import render
import ee
import json
import os
from django.http import JsonResponse
from .models import EventsInNeighbourhood, NeighbourhoodData, FlowerData, UserData, EventData
from .models import NeighbourhoodData, FlowerInNeighbourhood, CommunityMember
# Create your views here.
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializers import NeighbourhoodDataSerializer
from flower.serializers import FlowerDataSerializer
from user.serializer import User_Data_Serializer
from events.serialization import EventDataSerializer

# Create your views here.

# Initialize Google Earth Engine if credentials are available
try:
    ee.Authenticate()
    gee_project = os.getenv('GEE_PROJECT_ID', 'ee-methira19')
    ee.Initialize(project=gee_project)
    GEE_INITIALIZED = True
except Exception as e:
    print(f"Warning: Google Earth Engine not initialized: {e}")
    GEE_INITIALIZED = False

@api_view(['GET'])
def get_community_info(request):
    name = request.GET.get('name', '')
    try:
        neighbourhood = NeighbourhoodData.objects.get(neighbourhood_name=name)
    except NeighbourhoodData.DoesNotExist:
        return Response({'error': 'Could not find city'}, status=status.HTTP_400_BAD_REQUEST)

    neighbourhood_serializer = NeighbourhoodDataSerializer(neighbourhood)
    flowers = FlowerInNeighbourhood.objects.filter(neighbourhood_to_flower_fk=neighbourhood.n_id)
    members = CommunityMember.objects.filter(neighbourhood_to_member_fk=neighbourhood.n_id)
    events = EventsInNeighbourhood.objects.filter(neighbourhood_to_event_fk=neighbourhood.n_id)
    
    flowers_res = []
    for flower in flowers:
        flower_ser = FlowerDataSerializer(flower.flower_to_neighbourhood_fk)
        flowers_res.append(flower_ser.data)
    
    members_res = []
    for member in members:
        member_ser = User_Data_Serializer(member.member_to_neighbourhood_fk)
        members_res.append(member_ser.data)
    
    events_res = []
    for event in events:
        event_ser = EventDataSerializer(event.event_to_neightbourhood_fk)
        events_res.append(event_ser.data)
    
    
    
    
    
    response_data = {
        'neighbourhood': neighbourhood_serializer.data,
        'flowers': flowers_res,
        'members': members_res,
        'events': events_res,
    }
    
    return Response(response_data, status=status.HTTP_200_OK)
    

def interpolate_color(value):
    # Define the RGB values for white and green
    white = (255, 255, 255)
    green = (0, 255, 0)
    
    # Interpolate between white and green based on the adjusted value
    r = int(white[0] + (green[0] - white[0]) * value)
    g = int(white[1] + (green[1] - white[1]) * value)
    b = int(white[2] + (green[2] - white[2]) * value)

    # Convert RGB values to hex code
    hex_code = "#{:02x}{:02x}{:02x}".format(r, g, b)
    return hex_code

@api_view(['GET'])
def process_geoJSON(request):
    if not GEE_INITIALIZED:
        return JsonResponse({'error': 'Google Earth Engine not initialized. Set up GEE credentials to use this feature.'}, status=503)
    
    geojson_folder = '../geoJSON'
    if (geojson_folder):
        for file in os.listdir(geojson_folder):
            fp = os.path.join(geojson_folder, file)

            with open(fp, 'r') as f:
                geojson_content = json.load(f)
            neighbourhood_name = geojson_content["properties"]["name"]
            if NeighbourhoodData.objects.filter(neighbourhood_name=neighbourhood_name).exists():
                print(f"Neighbourhood {neighbourhood_name} already exists. Skipping...")
                continue  # Skip processing this GeoJSON file

            neighbourhood_f = ee.Feature(geojson_content)
            neighbourhood_fc = ee.FeatureCollection([neighbourhood_f])

            sentinel2 = ee.ImageCollection('COPERNICUS/S2_SR') \
                .filterBounds(neighbourhood_fc) \
                .filterDate('2023-01-01', '2023-12-31') \
                .median() \
                .clip(neighbourhood_fc)

            ndvi = sentinel2.normalizedDifference(['B8', 'B4'])

            #ndvi_masked = ndvi.clip(neighbourhood_fc)

            mean_ndvi = ndvi.reduceRegion(
                reducer=ee.Reducer.mean(),
                geometry=neighbourhood_fc,
                scale = 10,
            )
            mean_ndvi_value = mean_ndvi.getInfo()['nd'] * 10
            color = interpolate_color(mean_ndvi_value)
            print(mean_ndvi_value)
            neighbourhood_name = geojson_content["properties"]["name"]
            print(f"Mean NDVI for {neighbourhood_name}: {mean_ndvi_value}")
            neighbourhood = NeighbourhoodData.objects.create(
                ndvi = mean_ndvi_value,
                neighbourhood_name = neighbourhood_name,
                color = color,
                geoJSON = geojson_content
            )
            neighbourhood.save()

    return JsonResponse({'message': 'Mean NDVI calculation complete for all GeoJSON files.'})

@api_view(['GET'])
def hello_world(request):
    return Response({'message': 'Hello, world'})


@api_view(['GET'])
def get_all(request):
    try:
        results = []
        neighborhoods = NeighbourhoodData.objects.all()
        for neighborhood in neighborhoods:
            neighborhood_serialized = NeighbourhoodDataSerializer(neighborhood)
            results.append(neighborhood_serialized.data)
        res = {'neighbourhoods': results}
        # Serialize the queryset into JSON
        return Response(res, status=status.HTTP_200_OK)
    except Exception as e:
        return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)