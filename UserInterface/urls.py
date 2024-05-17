from django.urls import path
from UserInterface import views

urlpatterns = [
    path('courses', views.courses, name='lms courses'),
    path('login', views.login, name='lms login'),
]
