
from email import message
from urllib import response
from survey.models import Survey, Question, UserResponse
from survey.serializers import SurveySerializer, QuestionSerializer, UserResponseSerializer
from rest_framework.response import Response
from rest_framework import viewsets, permissions
from django.shortcuts import get_object_or_404

class SurveyViewSet(viewsets.ModelViewSet):

    queryset = Survey.objects.all()
    serializer_class = SurveySerializer

    def list(self, request):
        queryset = Survey.objects.all()
        serializer = SurveySerializer(queryset, many=True)
        return Response({"surveys": serializer.data})

    def destroy(self, request, *args, **kwargs):
        survey = self.get_object()
        message = f"Survey ID {survey.id} has been deleted"
        survey.delete()

        return Response({"message": message})

class QuestionViewSet(viewsets.ModelViewSet):
    
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer

    def list(self, request, survey_pk=None, *args, **kwargs):
        queryset = Question.objects.filter(survey=survey_pk)
        serializer = QuestionSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None, survey_pk=None):
        queryset = Question.objects.filter(pk=pk, survey=survey_pk)
        question = get_object_or_404(queryset, pk=pk)
        serializer = QuestionSerializer(question)
        return Response(serializer.data)

    def create(self, request, *args, **kwargs):
        survey_id = self.kwargs.get("survey_pk")
        question_data = request.data
        new_question = Question.objects.create(survey=Survey.objects.get(id=survey_id), question=question_data["question"])
        new_question.save()
        serializer = QuestionSerializer(new_question)
        return Response(serializer.data)

    def destroy(self, request, *args, **kwargs):
        question = self.get_object()
        message = f"Question {question.id} deleted"
        question.delete()

        return Response({"message": message})

class UserResponseViewSet(viewsets.ModelViewSet):

    queryset = UserResponse.objects.all()
    serializer_class = UserResponseSerializer

    def list(self, request, survey_pk=None, question_pk=None):
        queryset = UserResponse.objects.filter(question__survey=survey_pk, question=question_pk)
        serializer = UserResponseSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None, survey_pk=None, question_pk=None):
        queryset = UserResponse.objects.filter(pk=pk, question=question_pk, question__survey=survey_pk)
        response = get_object_or_404(queryset, pk=pk)
        serializer = UserResponseSerializer(response)
        return Response(serializer.data)
    
    def create(self, request, survey_pk=None, question_pk=None):
        response_data = request.data
        response_obj = UserResponse.objects.create(response=response_data["response"])
        question = Question.objects.get(pk=question_pk, survey=survey_pk)
        response_obj.save()
        question.responses.add(response_obj)
        serializer = UserResponseSerializer(response_obj)
        return Response(serializer.data)
