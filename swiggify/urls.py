from django.urls import path
from .views import GenerateRandomUserView

urlpatterns =[
    path('generate/', GenerateRandomUserView.as_view()),]