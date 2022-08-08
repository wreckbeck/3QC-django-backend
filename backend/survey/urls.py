
from django.urls import path, include
from survey.views import SurveyViewSet, UserResponseViewSet
from rest_framework.routers import DefaultRouter, SimpleRouter
from rest_framework_nested import routers

router = DefaultRouter()
router.register(r'surveys', SurveyViewSet, basename='surveys')

userresponse_router = routers.NestedSimpleRouter(
    router,
    r'surveys',
    lookup='survey')

userresponse_router.register(
    r'responses',
    UserResponseViewSet,
    basename='responses'
)

# response_router = routers.NestedSimpleRouter(
#     question_router,
#     r'questions',
#     lookup='question')

# response_router.register(
#     r'responses',
#     UserResponseViewSet,
#     basename='responses'
# )


urlpatterns = [
    path(r'', include(router.urls)),
    path(r'', include(userresponse_router.urls)),
    # path(r'', include(response_router.urls))
]