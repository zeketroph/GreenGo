from django.urls import path
from . import views


urlpatterns = [
    path('add-flower/', views.add_flower, name='add-flower'),
]