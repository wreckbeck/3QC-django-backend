
from survey.models import UserResponse, Question
from survey.serializers import UserResponseSerializer, QuestionSerializer
from rest_framework.response import Response
from rest_framework import viewsets

class UserResponseViewSet(viewsets.ModelViewSet):
    
    queryset = UserResponse.objects.all()
    serializer_class = UserResponseSerializer

    def create(self, request, *args, **kwargs):
        response_data = request.data

        new_question = Question.objects.create(
            question_1=response_data["user_responses"]["question_1"],
            question_2=response_data["user_responses"]["question_2"],
            question_3=response_data["user_responses"]["question_3"],
            question_4=response_data["user_responses"]["question_4"],
            question_5=response_data["user_responses"]["question_5"]
        )
        new_question.save()

        new_response = UserResponse.objects.create(user_responses=new_question)
        new_response.save()
        serializer = UserResponseSerializer(new_response)
        return Response(serializer.data)

    def destroy(self, request, *args, **kwargs):
        response = self.get_object()
        message = f"UserResponse {response.id} deleted"
        response.delete()

        return Response({"message": message})

class QuestionViewSet(viewsets.ModelViewSet):

    queryset = Question.objects.all()
    serializer_class = QuestionSerializer

