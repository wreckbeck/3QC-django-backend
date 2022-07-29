
from django.urls import path, include, re_path
from survey.views import SurveyViewSet, QuestionViewSet, AnswerViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register("questions", QuestionViewSet, basename="questions")
router.register("answers", AnswerViewSet, basename="answers")
router.register("", SurveyViewSet, basename='')

urlpatterns = [
    re_path('', include(router.urls))
]