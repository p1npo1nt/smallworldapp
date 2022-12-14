import datetime
from django.utils import timezone
from django.db import models
from django.contrib.auth.models import User

class FALN(models.Model):
    name = models.CharField(max_length=200)
    def __str__(self):
        return self.name

class ToDoList(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="todolist", null=True) # <--- added
    name = models.CharField(max_length=200)

    def __str__(self):
	    return self.name

class Futbol(models.Model):
    player_name = models.CharField(max_length=20)
    def __str__(self):
        return self.player_name

class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    def __str__(self):
        return self.question_text
    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    def __str__(self):
        return self.choice_text

class PpSize(models.Model):
    size_enter = models.CharField(max_length=20)
    def __str__(self):
        return self.size_enter

class UserInput(models.Model):
    iinput = models.CharField(max_length=100)
    def __str__(self):
        return self.iinput

# Create your models here.
