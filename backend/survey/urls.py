from django.urls import path
from survey import views
 
urlpatterns = [ 
    path('', views.SurveyList.as_view()),
    path('<int:id>', views.SurveyDetails.as_view()),
    path('<int:id>/questions', views.SurveyQuestions.as_view()),
    # path('<int:id>/questions', views.create_questions.as_view())
]