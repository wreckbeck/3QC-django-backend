

from rest_framework import serializers 
from survey.models import Survey, Question

# class AnswerSerializer(serializers.ModelSerializer):

#     class Meta:
#         model = Answer
#         fields = [
#                   'id',
#                   'answer',
#                   'question',]
#         depth = 1

class QuestionSerializer(serializers.ModelSerializer):
    
    survey = serializers.SlugRelatedField(
        read_only=True,
        slug_field='id'
    )
    class Meta:
        model = Question
        fields = ['survey',
                  'id',
                  'question']

class SurveySerializer(serializers.ModelSerializer):

    class Meta:
        model = Survey
        fields = ['id',
                  'name',
                  'created_on',
                  'updated_on',
                  'questions']

# class ResponseSerializer(serializers.ModelSerializer):
 
#     class Meta:
#         model = Response
#         fields = ['id',
#                   'user',
#                   'asnwer']