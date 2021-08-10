from django.db import models

# Create your models here.
class Points(models.Model):
    name = models.CharField(max_length=255)
    points = models.CharField(max_length=255)
    points_pair = models.CharField(max_length=255)

    def get_points(self):
        return 'The points ' + self.points + 'closest points' + self.points_pair + ' from ' + self.name

    def __str__(self):
        return self.name