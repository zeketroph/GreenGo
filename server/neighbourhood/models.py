from django.db import models
from flower.models import FlowerData
from user.models import UserData
from events.models import EventData

class NeighbourhoodData(models.Model):
    ndvi = models.FloatField(default=0)
    neighbourhood_name = models.CharField(max_length=200, default="")
    color = models.CharField(max_length=7, default="#FFFFFF")
    geoJSON = models.JSONField("geoJSON")
    n_id = models.AutoField(primary_key=True)


    def __str__(self):
        return f"{self.neighbourhood_name}"

class CommunityMember(models.Model):
    member_to_neighbourhood_fk = models.ForeignKey(UserData, max_length=1000, to_field='u_id', on_delete=models.CASCADE)
    neighbourhood_to_member_fk = models.ForeignKey(NeighbourhoodData, to_field='n_id', on_delete=models.CASCADE)
    def __str__(self):
        return f"{self.member_to_neighbourhood_fk}, {self.neighbourhood_to_member_fk}"

    def __str__(self):
        return f"{self.member_to_neighbourhood_fk}, {self.neighbourhood_to_member_fk}"

    def __str__(self):
        return f"{self.member_to_neighbourhood_fk}, {self.neighbourhood_to_member_fk}"

class FlowerInNeighbourhood(models.Model):
    flower_to_neighbourhood_fk = models.ForeignKey(FlowerData, max_length=1000, to_field='f_id', on_delete=models.CASCADE)
    neighbourhood_to_flower_fk = models.ForeignKey(NeighbourhoodData, max_length=1000, to_field='n_id', on_delete=models.CASCADE)
    
    def __str__(self):
        return f"{self.flower_to_neighbourhood_fk}, {self.neighbourhood_to_flower_fk}"


class EventsInNeighbourhood(models.Model):
    event_to_neightbourhood_fk = models.ForeignKey(EventData, to_field='e_id', on_delete=models.CASCADE)
    neighbourhood_to_event_fk = models.ForeignKey(NeighbourhoodData, to_field='n_id', on_delete=models.CASCADE)
    
    def __str__(self):
        return f"{self.event_to_neightbourhood_fk}, {self.neighbourhood_to_event_fk}"