

from survey.models import Survey, Question, Answer
from survey.serializers import SurveySerializer, QuestionSerializer, AnswerSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, viewsets
from rest_framework.decorators import action




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

    def create(self, request, *args, **kwargs):
        question_data = request.data
        new_question = Question.objects.create(survey=Survey.objects.get(id=question_data["survey"]), question=question_data["question"])
        new_question.save()
        serializer = QuestionSerializer(new_question)
        return Response(serializer.data)

    def destroy(self, request, *args, **kwargs):
        question = self.get_object()
        question.delete()

        return Response({"message": f"Item {question.id} has been deleted"})

class AnswerViewSet(viewsets.ModelViewSet):
    
    queryset = Answer.objects.all()
    serializer_class = AnswerSerializer
    
    def create(self, request, *args, **kwargs):
        answer_data = request.data
        new_answer = Answer.objects.create(question=Question.objects.get(id=answer_data["question"]), answer=answer_data["answer"])
        new_answer.save()
        serializer = AnswerSerializer(new_answer)
        return Response(serializer.data)


    def destroy(self, request, *args, **kwargs):
        answer = self.get_object()
        answer.delete()

        return Response({"message": f"Item {answer.id} has been deleted"})