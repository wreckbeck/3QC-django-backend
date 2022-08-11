
from django.db import models


class Question(models.Model):
    question_1 = models.IntegerField(default=0)
    question_2 = models.IntegerField(default=0)
    question_3 = models.IntegerField(default=0)
    question_4 = models.IntegerField(default=0)
    question_5 = models.IntegerField(default=0)

class UserResponse(models.Model):
    user_responses = models.OneToOneField(Question, on_delete=models.CASCADE, null=True)

