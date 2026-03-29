import json
from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import FlowerData
from neighbourhood.models import FlowerInNeighbourhood, NeighbourhoodData
from django.core.files.base import ContentFile
import base64
from botocore.config import Config
import os
from dotenv import load_dotenv
from rest_framework import status
import time
@api_view(['POST'])
def add_flower(request):
   # Get the file and community from the request
    file_data = request.FILES.get('file')
    community = request.POST.get('community')



    # Create FlowerData instance with the image
    flower = FlowerData(image=file_data)
    flower.save()
    time.sleep(10)    
    community = NeighbourhoodData.objects.get(neighbourhood_name=community)
    print(community)
    FlowerInNeighbourhood(neighbourhood_to_flower_fk=community, flower_to_neighbourhood_fk=flower).save()
    
    path = "/Users/hasithdealwis/Library/Mobile Documents/com~apple~CloudDocs/MonsTerra-SaaS/uottahack2024/server/media/images/image_04081_CRZXSwa.jpg"
    flower.name = main(os.path.abspath("../server"+flower.image.url))
    flower.save()
    return Response({'message': 'Successfully uploaded picture!'}, status=status.HTTP_200_OK)

#Copyright 2018 Amazon.com, Inc. or its affiliates. All Rights Reserved.
#PDX-License-Identifier: MIT-0 (For details, see https://github.com/awsdocs/amazon-rekognition-developer-guide/blob/master/LICENSE-SAMPLECODE.)

import boto3

def detect_labels_local_file(photo):
    my_config = Config(
        region_name="us-east-2"
    )
    load_dotenv()
    client=boto3.client('rekognition', config=my_config)
   
    with open(photo, 'rb') as image:
        response = client.detect_labels(Image={'Bytes': image.read()})
        
    print('Detected labels in ' + photo)  
    print(response['Labels'])  
    for label in response['Labels']:
        return label

def main(p):
    photo=p

    return detect_labels_local_file(photo)
    


if __name__ == "__main__":
    main()

