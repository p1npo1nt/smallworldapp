from django.db import models

class User(models.Model):
    name = models.CharField(max_length=200) 
    email = models.CharField(max_length=200)

    def __str__(self):
        return self.name + " " + self.email #returns its values
