from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class Survey(models.Model):
    name = models.CharField(max_length=100, default='Survey Name')
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

class Answer(models.Model):
    answer = models.IntegerField(default=0)

class Question(models.Model):
    survey = models.ForeignKey(Survey, on_delete=models.CASCADE, null=True, related_name='questions')
    question = models.TextField(default='')
    answers = models.ManyToManyField(Answer)



# class Response(models.Model):
#     question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='responses')
#     answer = models.ForeignKey(Answer, on_delete=models.CASCADE, related_name='responses')