
from rest_framework import serializers 
from survey.models import UserResponse, Question


class QuestionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Question
        fields = ['id',
                    'question_1',
                    'question_2',
                    'question_3',
                    'question_4',
                    'question_5']

class UserResponseSerializer(serializers.ModelSerializer):

    class Meta:
        model = UserResponse
        fields = ['id',
                    'user_responses']
        depth=1


