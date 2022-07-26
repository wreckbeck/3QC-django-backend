from rest_framework import serializers 
from survey.models import Survey, Answer, Question, UserAnswer

class SurveySerializer(serializers.ModelSerializer):
 
    class Meta:
        model = Survey
        fields = ['id',
                  'name',
                  'created_on',
                  'updated_on']

class AnswerSerializer(serializers.ModelSerializer):
 
    class Meta:
        model = Answer
        fields = ('id',
                  'question',
                  'answer_text')

class QuestionSerializer(serializers.ModelSerializer):
 
    class Meta:
        model = Question
        fields = ('id',
                  'survey',
                  'question_text')

class UserAnswerSerializer(serializers.ModelSerializer):
 
    class Meta:
        model = UserAnswer
        fields = ('id',
                  'user',
                  'asnwer')