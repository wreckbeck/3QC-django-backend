
from unicodedata import name
from survey.models import Survey, Question
from django.http import Http404
from survey.serializers import SurveySerializer, QuestionSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


# CLASS-BASED Views, Django REST Framework

# GET all Survey's and POST new Survey
class list_surveys(APIView):

    def get(self, request, format=None):
        surveys = Survey.objects.all()
        serializer = SurveySerializer(surveys, many=True)
        return Response({'surveys': serializer.data})

    def post(self, request, format=None):
        serializer = SurveySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

# GET single survey, PUT a Survey, DELETE a survey
class survey_details(APIView):

    def get_object(self, id):
        try:
            return Survey.objects.get(pk=id)
        except Survey.DoesNotExist:
            raise Http404

    def get(self, request, id, format=None):
        survey = self.get_object(id)
        serializer = SurveySerializer(survey)
        return Response(serializer.data)

    def put(self, request, id, format=None):
        survey = self.get_object(id)
        serializer = SurveySerializer(survey, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    def delete(self, request, id, format=None):
        survey = self.get_object(id)
        survey.delete()
        return Response({'message': f'Survey {survey.name} deleted'}, status=204)

class list_survey_questions(APIView):
    
    def get(self, request, id, format=None):
        questions = Survey.objects.get(pk=id).questions.all()
        survey_name = Survey.objects.get(pk=id).name
        serializer = QuestionSerializer(questions, many=True)
        return Response({f'Survey {survey_name}': {
            'questions': serializer.data}})

class create_survey_questions(APIView):
    
    def post(self, request, format=None):
        serializer = QuestionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)