from django.urls import path
from Grades import views 


urlpatterns = [ 
               
    path('grades', views.grades, name='grades'), 
               
               ]