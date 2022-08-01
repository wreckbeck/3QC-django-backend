
from django.urls import path, include
from survey.views import SurveyViewSet, QuestionViewSet, UserResponseViewSet
from rest_framework.routers import DefaultRouter, SimpleRouter
from rest_framework_nested import routers



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

response_router = routers.NestedSimpleRouter(
    question_router,
    r'questions',
    lookup='questions')

response_router.register(
    r'responses',
    UserResponseViewSet,
    basename='survey-responses'
)


urlpatterns = [
    path('', include(router.urls)),
    path('', include(question_router.urls)),
    path('', include(response_router.urls))
]