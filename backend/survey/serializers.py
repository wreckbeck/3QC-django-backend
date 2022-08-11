
from rest_framework import serializers 
from survey.models import Survey, UserResponse, Question


class QuestionSerializer(serializers.ModelSerializer):
    parent_lookup_kwargs = {
    'question_pk': 'question__pk',
    'survey_pk': 'question__survey__pk',
    }

    class Meta:
        model = Question
        fields = ['id',
                    'question_1',
                    'question_2',
                    'question_3',
                    'question_4']
                    # 'question_5']



class UserResponseSerializer(serializers.ModelSerializer):
    parent_lookup_kwargs = {
    'survey_pk': 'survey__pk',
    }

    class Meta:
        model = UserResponse
        fields = ['id',
                    'user_responses']
        depth=1

class SurveySerializer(serializers.ModelSerializer):
    class Meta:
        model = Survey
        fields = ['id',
                  'name',
                  'created_on',
                  'updated_on',
                  'responses']
