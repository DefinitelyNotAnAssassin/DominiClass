from django.urls import path 
from Course import views 


urlpatterns = [
    
    
    path('course/enroll/', views.enroll, name='enroll'),
    path('course/getCourse', views.getCourse, name='getCourse'),
    path('course/getCourse/<str:course_id>', views.getExactCourse, name='getExactCourse'),
    path('course/lesson/<str:lesson_id>', views.lesson, name='lesson'),
    path('course/activity/<str:activity_id>', views.exact_activity, name='activity'),
    path('course/submitActivity/<str:activity_id>', views.submit_activity, name='activity'),
    path('course/submitActivity/<str:activity_id>', views.submit_activity, name='activity'),
    path('course/getMissingActivities', views.getMissingActivities, name='getMissingActivities'),
    path('course/getFinishedActivities', views.getFinishedActivities, name='getMissingActivities'),
    
]   