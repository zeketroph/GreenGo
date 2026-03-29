from django.db import models

# Create your models here.
class FlowerData(models.Model):
    
    image = models.ImageField(upload_to='images')  

    name = models.CharField(max_length=100, default="")
    #picture = models
    f_id = models.AutoField(primary_key=True)
    
    #Location
    location = models.CharField(max_length=200, default="")
    
    
    def __str__(self):
        return f"{self.name} found at {self.location}"
    

