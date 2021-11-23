from django.db import models


class Family(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name


class Animal(models.Model):
    name = models.CharField(max_length=30)
    legs = models.IntegerField()
    weight = models.FloatField(max_length=500)
    height = models.FloatField(max_length=300)
    speed = models.FloatField(max_length=30)
    family = models.ForeignKey(Family, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
