
from urllib import response
from survey.models import Survey, Question, UserResponse
from survey.serializers import SurveySerializer, QuestionSerializer, UserResponseSerializer
from rest_framework.response import Response
from rest_framework import viewsets, permissions
from rest_framework.exceptions import NotFound
from django.shortcuts import get_object_or_404

class SurveyViewSet(viewsets.ModelViewSet):

    queryset = Survey.objects.all()
    serializer_class = SurveySerializer

    def destroy(self, request, *args, **kwargs):
        survey = self.get_object()
        survey.delete()

        return Response({"message": f"Item {survey.name} has been deleted"})

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

    # def get_queryset(self, *args, **kwargs):
    #     survey_id = self.kwargs.get("survey_pk")
    #     try:
    #         survey = Survey.objects.get(id=survey_id)
    #     except Survey.DoesNotExist:
    #         raise NotFound('A survey with this id does not exist')
    #     return self.queryset.filter(survey=survey)

    def create(self, request, *args, **kwargs):
        survey_id = self.kwargs.get("survey_pk")
        question_data = request.data
        new_question = Question.objects.create(survey=Survey.objects.get(id=survey_id), question=question_data["question"])
        new_question.save()
        serializer = QuestionSerializer(new_question)
        return Response(serializer.data)

    def destroy(self, request, *args, **kwargs):
        question_id = self.kwargs.get("question_pk")
        question = self.get_object()
        question.delete()

        return Response({"message": f"Item {question_id} has been deleted"})

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
    
    def create(self, request, survey_pk=None, *args, **kwargs):
        question_pk = self.kwargs.get("question_pk")
        question = Question.objects.get(pk=question_pk, survey=survey_pk)
        response_data = request.data
        new_response = UserResponse.objects.create(question=question, response=response_data["response"])
        new_response.save()
        serializer = UserResponseSerializer(new_response)
        return Response(serializer.data)

    # queryset = UserResponse.objects.all().select_related(
    #     'question'
    #     )

    # def get_queryset(self, *args, **kwargs):
    #     question_id = self.kwargs.get("question_pk")
    #     try:
    #         question = Question.objects.get(id=question_id)
    #     except Question.DoesNotExist:
    #         raise NotFound('A question with this id does not exist')
    #     return self.queryset.filter(question=question)
