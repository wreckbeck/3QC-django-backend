from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class Survey(models.Model):
    name = models.CharField(max_length=100, default='Survey Name')
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)


class Question(models.Model):
    survey = models.ForeignKey(Survey, on_delete=models.CASCADE, null=True, related_name='questions')
    question = models.TextField(default='')


class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE, null=True, related_name='answers')
    answer = models.TextField(default='')

class UserAnswer(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    answer = models.ForeignKey(Answer, on_delete=models.CASCADE)