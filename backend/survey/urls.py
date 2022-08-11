
from django.urls import path, include
from survey.views import UserResponseViewSet
from rest_framework.routers import DefaultRouter
from rest_framework_nested import routers

router = DefaultRouter()
router.register(r'responses', UserResponseViewSet, basename='responses')

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
    path(r'', include(router.urls))
]