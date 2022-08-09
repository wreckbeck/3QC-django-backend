
from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class Survey(models.Model):
    name = models.CharField(max_length=100, default='Survey Name')
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)



class Question(models.Model):
    question_1 = models.IntegerField()
    question_2 = models.IntegerField()
    question_3 = models.IntegerField()
    question_4 = models.IntegerField()

class UserResponse(models.Model):
    survey = models.ForeignKey(Survey, on_delete=models.CASCADE, null=True, related_name='responses')
    user_responses = models.OneToOneField(Question, on_delete=models.CASCADE)

