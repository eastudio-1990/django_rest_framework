from django.urls import path
from . import views

app_name = 'home'

urlpatterns=[
   path('', views.Home.as_view(), name='home'), #endpoints
   path('questions/',views.QuestionView.as_view()),
   #path('answers/',views.AnswerView.as_view()),
]

 