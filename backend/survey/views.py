
from survey.models import Survey
from survey.serializers import SurveySerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, viewsets




class SurveyViewSet(viewsets.ModelViewSet):

    queryset = Survey.objects.all()
    serializer_class = SurveySerializer

    def destroy(self, request, *args, **kwargs):
        survey = self.get_object()
        survey.delete()

        return Response({"message": f"Item {survey.name} has been deleted"})

