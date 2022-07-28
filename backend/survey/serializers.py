

from rest_framework import serializers 
from survey.models import Survey, Answer, Question, UserAnswer

class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = ['id',
                  'question']

class SurveySerializer(serializers.ModelSerializer):
    questions = QuestionSerializer(many=True)
    
    class Meta:
        model = Survey
        fields = ['id',
                  'name',
                  'created_on',
                  'updated_on',
                  'questions']
    
    def create(self, validated_data):
        questions = validated_data.pop('questions')
        survey_instance = Survey.objects.create(**validated_data)
        for question in questions:
            Question.objects.create(survey=survey_instance,**question)
        return survey_instance

class AnswerSerializer(serializers.ModelSerializer):
 
    class Meta:
        model = Answer
        fields = ['id',
                  'answer']


class UserAnswerSerializer(serializers.ModelSerializer):
 
    class Meta:
        model = UserAnswer
        fields = ['id',
                  'user',
                  'asnwer']