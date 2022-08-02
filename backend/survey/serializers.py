
from rest_framework import serializers 
from survey.models import Survey, Question, UserResponse

class UserResponseSerializer(serializers.ModelSerializer):
    parent_lookup_kwargs = {
    'question_pk': 'question__pk',
    'survey_pk': 'question__survey__pk',
    }

    class Meta:
        model = UserResponse
        fields = ['id',
                    'response']

class QuestionSerializer(serializers.ModelSerializer):

    parent_lookup_kwargs = {
        'survey_pk': 'survey__pk'
    }

    class Meta:
        model = Question
        fields = ['survey',
                  'id',
                  'question',
                  'responses']

class SurveySerializer(serializers.ModelSerializer):
    class Meta:
        model = Survey
        fields = ['id',
                  'name',
                  'created_on',
                  'updated_on',
                  'questions']
