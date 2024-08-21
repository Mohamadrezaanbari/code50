from django.db import models


class Profession(models.Model):
    title = models.CharField(max_length=40)

    def __str__(self):
        return self.title


class User(models.Model):
    uid = models.IntegerField(primary_key=True)
    firstName = models.CharField(max_length=50)
    lastName = models.CharField(max_length=50)
    age = models.IntegerField(default=0)
    profession = models.CharField(max_length=50)
    Address = models.CharField(max_length=200)
