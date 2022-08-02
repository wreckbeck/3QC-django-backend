
from django.urls import path, include
from survey.views import SurveyViewSet, QuestionViewSet, UserResponseViewSet
from rest_framework.routers import DefaultRouter, SimpleRouter
from rest_framework_nested import routers

router = DefaultRouter()
router.register(r'surveys', SurveyViewSet, basename='surveys')

question_router = routers.NestedSimpleRouter(
    router,
    r'surveys',
    lookup='survey')

question_router.register(
    r'questions',
    QuestionViewSet,
    basename='questions'
)

response_router = routers.NestedSimpleRouter(
    question_router,
    r'questions',
    lookup='question')

response_router.register(
    r'responses',
    UserResponseViewSet,
    basename='responses'
)


urlpatterns = [
    path(r'', include(router.urls)),
    path(r'', include(question_router.urls)),
    path(r'', include(response_router.urls))
]