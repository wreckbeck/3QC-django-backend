


from http.client import responses
from rest_framework import serializers 
from survey.models import Survey, Question, UserResponse

class UserResponseSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserResponse
        fields = ['id',
                    'response']

class QuestionSerializer(serializers.ModelSerializer):
    
    survey = serializers.SlugRelatedField(
        read_only=True,
        slug_field='id'
    )
    responses = serializers.SlugRelatedField(
        many=True,
        read_only=True,
        slug_field='id'
    )

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
