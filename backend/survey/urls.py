from django.urls import path, include
from survey.views import SurveyViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r"surveys", SurveyViewSet)

urlpatterns = router.urls