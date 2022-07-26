from urllib import response
from django.shortcuts import render
from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser 
from rest_framework import status
from survey.models import Survey
from survey.serializers import SurveySerializer
from rest_framework.decorators import api_view


@api_view(['GET', 'POST'])
def survey_data(request):
    if request.method == 'GET':
        survey = Survey.objects.get_queryset()
        survey_serializer = SurveySerializer(survey)
        return JsonResponse(survey_serializer.data, safe=False, status=status.HTTP_200_OK) # 'the safe boolean parameter defaults to True. If it’s set to False, any object can be passed for serialization (otherwise only dict instances are allowed)'
    elif request.method == 'POST':
        survey_data = JSONParser().parse(request)
        survey_serializer = SurveySerializer(data=survey_data)
        if survey_serializer.is_valid():
            survey_serializer.save()
            return JsonResponse(survey_serializer.data, status=status.HTTP_201_CREATED) 
        return JsonResponse(survey_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    return JsonResponse(survey_serializer.data, status=status.HTTP_400_NOT_FOUND)