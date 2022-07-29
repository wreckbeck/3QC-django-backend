from posixpath import basename
from django.urls import path, include
from survey.views import SurveyViewSet, QuestionViewSet, AnswerViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register("surveys", SurveyViewSet)
router.register("questions", QuestionViewSet)
router.register("answers", AnswerViewSet)

urlpatterns = router.urls