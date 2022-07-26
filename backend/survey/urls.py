from django.urls import path
from survey import views
 
urlpatterns = [ 
    path('', views.survey_data),
    # url(r'^api/tutorials/(?P<pk>[0-9]+)$', views.tutorial_detail),
    # url(r'^api/tutorials/published$', views.tutorial_list_published)
]