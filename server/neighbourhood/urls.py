from django.urls import path
from . import views


urlpatterns = [
    path('process-geoJSON/', views.process_geoJSON, name='process_geoJSON'),
    path('hello-world/', views.hello_world, name='hello-world'),
    path('get-community-info/', views.get_community_info, name='get-community-info'),
    path('get-all/', views.get_all, name='get-all')
]