from urllib import response
from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class Survey(models.Model):
    name = models.CharField(max_length=100, default='Survey Name')
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

class UserResponse(models.Model):
    response = models.IntegerField(default=0)

class Question(models.Model):
    survey = models.ForeignKey(Survey, on_delete=models.CASCADE, null=True, related_name='questions')
    question = models.TextField(default='')
    responses = models.ManyToManyField(UserResponse)


