from django.db import models


class Album(models.Model):
    title = models.CharField(max_length=65)
    artist = models.ForeignKey('Artist', on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class Artist(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Track(models.Model):
    title = models.CharField(max_length=255)

    def __str__(self):
        return self.title