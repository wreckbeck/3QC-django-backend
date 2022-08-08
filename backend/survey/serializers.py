
from rest_framework import serializers 
from survey.models import Survey, UserResponse

class UserResponseSerializer(serializers.ModelSerializer):
    parent_lookup_kwargs = {
    'survey_pk': 'survey__pk',
    }

    class Meta:
        model = UserResponse
        fields = ['id',
                    'response']

class SurveySerializer(serializers.ModelSerializer):
    class Meta:
        model = Survey
        fields = ['id',
                  'name',
                  'created_on',
                  'updated_on',
                  'responses']
