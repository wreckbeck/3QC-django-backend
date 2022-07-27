
from survey.models import Survey
from django.http import Http404
from survey.serializers import SurveySerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


# CLASS-BASED Views, Django REST Framework

# GET all Survey's and POST new Survey
class SurveyList(APIView):

    def get(self, request, format=None):
        surveys = Survey.objects.all()
        serializer = SurveySerializer(surveys, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = SurveySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

# GET single survey, PUT a Survey, DELETE a survey
class SurveyDetail(APIView):

    def get_object(self, pk):
        try:
            return Survey.objects.get(pk=pk)
        except Survey.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        survey = self.get_object(pk)
        serializer = SurveySerializer(survey)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        survey = self.get_object(pk)
        serializer = SurveySerializer(survey, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    def delete(self, request, pk, format=None):
        survey = self.get_object(pk)
        survey.delete()
        return Response({'message': f'{survey.id} deleted'}, status=204)

    