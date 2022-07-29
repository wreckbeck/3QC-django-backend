from survey.models import Survey, Question, Answer
from survey.serializers import SurveySerializer, QuestionSerializer, AnswerSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import viewsets

class SurveyViewSet(viewsets.ModelViewSet):

    queryset = Survey.objects.all()
    serializer_class = SurveySerializer

    def list(self, request):
        queryset = Survey.objects.all()
        serializer = SurveySerializer(queryset, many=True)
        return Response({"surveys": serializer.data})

    def destroy(self, request, *args, **kwargs):
        survey = self.get_object()
        survey.delete()

        return Response({"message": f"Item {survey.name} has been deleted"})

class QuestionViewSet(viewsets.ModelViewSet):
    
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer

    def list(self, request):
        queryset = Question.objects.all()
        serializer = QuestionSerializer(queryset, many=True)
        return Response({"questions": serializer.data})

    def create(self, request, *args, **kwargs):
        question_data = request.data
        new_question = Question.objects.create(survey=Survey.objects.get(id=question_data["survey"]), question=question_data["question"])
        new_question.save()

        for answer in question_data["answers"]:
            answer_obj = Answer.objects.get(answer=answer["answer"])
            new_question.answers.add(answer_obj)
        
        serializer = QuestionSerializer(new_question)
        return Response(serializer.data)

    def destroy(self, request, *args, **kwargs):
        question = self.get_object()
        question.delete()

        return Response({"message": f"Item {question} has been deleted"})

class AnswerViewSet(viewsets.ModelViewSet):
    
    queryset = Answer.objects.all()
    serializer_class = AnswerSerializer
    
    def list(self, request):
        queryset = Answer.objects.all()
        serializer = AnswerSerializer(queryset, many=True)
        return Response({"answers": serializer.data})

    def destroy(self, request, *args, **kwargs):
        answer = self.get_object()
        answer.delete()

        return Response({"message": f"Item {answer.id} has been deleted"})

