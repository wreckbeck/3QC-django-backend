

from rest_framework import serializers 
from survey.models import Survey, Answer, Question, ResponseObject

class AnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Answer
        fields = [
            'id',
            'answer'
            ]

class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = [
            'id',
            'question',
            'answers'
            ]
        depth = 1

class SurveySerializer(serializers.ModelSerializer):
    class Meta:
        model = Survey
        fields = [
            'id',
            'name',
            'created_on',
            'updated_on',
            'questions'
            ]
        depth = 1

class ResponseSerializer(serializers.ModelSerializer):
    class Meta:
        model = ResponseObject
        fields = [
            'id',
            'questions',
            'selected_answers'
            ]
        depth = 1