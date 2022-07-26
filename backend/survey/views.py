from django.shortcuts import render
from survey.models import Survey
from rest_framework import viewsets
# from rest_framework import permissions
from survey.serializers import SurveySerializer

# Create your views here.
class SurveyViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Survey.objects.all()
    serializer_class = SurveySerializer
    # permission_classes = [permissions.IsAuthenticated]