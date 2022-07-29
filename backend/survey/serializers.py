

from rest_framework import serializers 
from survey.models import Survey, Answer, Question

class AnswerSerializer(serializers.ModelSerializer):

    class Meta:
        model = Answer
        fields = [
                  'id',
                  'answer',
                  'question',]
        depth = 1

class QuestionSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Question
        fields = [
                  'id',
                  'question',
                  'answers']
        depth = 1

class SurveySerializer(serializers.ModelSerializer):

    class Meta:
        model = Survey
        fields = ['id',
                  'name',
                  'created_on',
                  'updated_on',
                  'questions']
        depth = 1

# class ResponseSerializer(serializers.ModelSerializer):
 
#     class Meta:
#         model = Response
#         fields = ['id',
#                   'user',
#                   'asnwer']