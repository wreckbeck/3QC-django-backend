from survey.models import Survey
from rest_framework import serializers


class SurveySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Survey
        fields = ['id', 'name', 'created_on', 'updated_on']