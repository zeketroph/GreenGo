from django.test import TestCase
from django.urls import reverse
from rest_framework import status

class ProcessGeoJSONTestCase(TestCase):
    def test_process_geoJSON(self):
        
        # Make a POST request to the process_geoJSON endpoint
        response = self.client.get(reverse('process_geoJSON'))

        # Check that the response status code is 200 (OK)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        # You can add additional assertions here to validate the response content
        print('Received response:', response.json())
