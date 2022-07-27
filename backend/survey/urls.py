from django.urls import path
from survey import views
 
urlpatterns = [ 
    path('', views.SurveyList.as_view()),
    path('<int:pk>', views.SurveyDetail.as_view())
]