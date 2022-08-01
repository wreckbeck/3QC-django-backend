
from django.urls import path, include
from survey.views import SurveyViewSet, QuestionViewSet
from rest_framework.routers import DefaultRouter, SimpleRouter
from rest_framework_nested import routers

# router = DefaultRouter()
# router.register("surveys", SurveyViewSet)
# router.register("questions", QuestionViewSet)

router = SimpleRouter()
router.register('surveys', SurveyViewSet)

question_router = routers.NestedSimpleRouter(
    router,
    r'surveys',
    lookup='survey')

question_router.register(
    r'questions',
    QuestionViewSet,
    basename='survey-question'
)

urlpatterns = [
    path('', include(router.urls)),
    path('', include(question_router.urls)),
]