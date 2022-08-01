
from survey.models import Survey, Question, UserResponse
from survey.serializers import SurveySerializer, QuestionSerializer, UserResponseSerializer
from rest_framework.response import Response
from rest_framework import viewsets
from rest_framework.exceptions import NotFound

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

    queryset = Question.objects.all().select_related(
        'survey'
        )
    serializer_class = QuestionSerializer

    def get_queryset(self, *args, **kwargs):
        survey_id = self.kwargs.get("survey_pk")
        try:
            survey = Survey.objects.get(id=survey_id)
        except Survey.DoesNotExist:
            raise NotFound('A survey with this id does not exist')
        return self.queryset.filter(survey=survey)

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
