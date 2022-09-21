from django.db import models

# Create your models here.

class Director(models.Model):
    name = models.CharField(max_length=255)


    def __str__(self):
        return self.name



class Movie(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    duration = models.CharField(max_length=255)
    director = models.ForeignKey(Director, on_delete = models.CASCADE)



class Review(models.Model):
    text = models.TextField()
    movie = models.ForeignKey(Movie, on_delete = models.CASCADE)