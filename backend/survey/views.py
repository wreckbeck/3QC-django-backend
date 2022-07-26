

from survey.models import Survey
from survey.serializers import SurveySerializer
from rest_framework import generics



# @api_view(['GET', 'POST'])
# def survey_list(request):
#     if request.method == 'GET':
#         surveys = Survey.objects.all()
#         serializer = SurveySerializer(surveys, many=True) # must set many = true to let drf know that the object is a list of items that needs to be serialized
#         return JsonResponse(serializer.data, safe=False) # 'the safe boolean parameter defaults to True. If it’s set to False, any object can be passed for serialization (otherwise only dict instances are allowed)'
   
#     elif request.method == 'POST':
#         survey_data = JSONParser().parse(request)
#         serializer = SurveySerializer(data=survey_data)
#         if serializer.is_valid():
#             serializer.save()
#             return JsonResponse(serializer.data, status=201)
#         return JsonResponse(serializer.errors, status=404)
# ------------------------------------------------------------------------------------
# ------------------------------------------------------------------------------------
    # def get(self, request, format=None):
    #     surveys = Survey.objects.all()
    #     serializer = SurveySerializer(surveys, many=True)
    #     return Response(serializer.data)
    # def post(self, request, format=None):
    #     serializer = SurveySerializer(data=request.data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data, status=201)
    #     return Response(serializer.errors, status=400)

class SurveyList(generics.ListCreateAPIView):
    queryset = Survey.objects.all()
    serializer_class = SurveySerializer
    
class SurveyDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Survey.objects.all()
    serializer_class = SurveySerializer
    