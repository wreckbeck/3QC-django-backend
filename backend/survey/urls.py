from django.urls import path
from survey import views
 
urlpatterns = [ 
    path('', views.list_surveys.as_view()),
    path('<int:id>', views.survey_details.as_view()),
    path('<int:id>/questions', views.list_survey_questions.as_view()),
    # path('<int:id>/questions', views.create_questions.as_view())
]