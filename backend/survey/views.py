from urllib import response
from survey.models import Survey, Question, Answer, ResponseObject
from survey.serializers import SurveySerializer, QuestionSerializer, AnswerSerializer, ResponseSerializer
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

class ResponseViewSet(viewsets.ModelViewSet):
    
    queryset = ResponseObject.objects.all()
    serializer_class = ResponseSerializer

    # def list(self, request):
    #     queryset = Response.objects.all()
    #     serializer = ResponseSerializer(queryset, many=True)
    #     return Response({"responses": serializer.data})

    def create(self, request, *args, **kwargs):
        response_data = request.data
        new_response = ResponseObject.objects.create(survey=Survey.objects.get(id=response_data["survey"]))
        new_response.save()

        for question in response_data["questions"]:
            question_obj = Question.objects.get(question=question["question"])
            new_response.answers.add(question_obj)
        
        for answer in response_data["selected_answers"]:
            answer_obj = Answer.objects.get(answer=answer["answer"])
            new_response.answers.add(answer_obj)
        
        serializer = ResponseSerializer(new_response)
        return Response(serializer.data)

    def destroy(self, request, *args, **kwargs):
        response_obj = self.get_object()
        response_obj.delete()

        return Response({"message": f"Item {response_obj} has been deleted"})