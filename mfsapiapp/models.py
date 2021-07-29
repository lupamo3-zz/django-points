from django.db import models

# Create your models here.
class Points(models.Model):
    name = models.CharField(max_length=255)
    points = models.CharField(max_length=255)
    points_pair = models.CharField(max_length=255)


    def __str__(self):
        return self.name