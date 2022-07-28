

from rest_framework import serializers 
from survey.models import Survey, Answer, Question, UserAnswer

class AnswerSerializer(serializers.ModelSerializer):

    class Meta:
        model = Answer
        fields = ['id',
                  'answer']

class QuestionSerializer(serializers.ModelSerializer):
    answers = AnswerSerializer(many=True)
    
    class Meta:
        model = Question
        fields = ['id',
                  'question',
                  'answers']
    
    def create(self, validated_data):
        answers = validated_data.pop('answers')
        question_instance = Question.objects.create(**validated_data)
        for answer in answers:
            Answer.objects.create(quesion=question_instance,**answer)
        return question_instance

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



class UserAnswerSerializer(serializers.ModelSerializer):
 
    class Meta:
        model = UserAnswer
        fields = ['id',
                  'user',
                  'asnwer']