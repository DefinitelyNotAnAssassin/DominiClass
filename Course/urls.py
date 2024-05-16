from django.urls import path 
from Course import views 


urlpatterns = [
    
    path('course/<str:course_code', views.course, name='course'), # /course/IT101
    path('course/<str:course_code>/material', views.course_material, name='course_material'), # /course/IT101/material
    path('course/<str:course_code>/activity', views.course_activity, name='course_activity'), # /course/IT101/activity
    path('course/<str:course_code>/activity/<int:activity_id>', views.activity, name='activity'), # /course/IT101/activity/1
    path('course/<str:course_code>/activity/<int:activity_id>/submission', views.submission, name='submission'), # /course/IT101/activity/1/submission
    path('course/<str:course_code>/activity/<int:activity_id>/submission/<int:submission_id>', views.submission, name='submission'), # /course/IT101/activity/1/submission/1]
    path('course/enroll/', views.enroll, name='enroll'),
    path('course/getCourse', views.getCourse, name='getCourse'),
    path('course/getCourse/<str:course_id>', views.getExactCourse, name='getExactCourse'),
    path('course/lesson/<str:lesson_id>', views.lesson, name='lesson'),
    path('course/activity/<str:activity_id>', views.exact_activity, name='activity'),
    path('course/submitActivity/<str:activity_id>', views.submit_activity, name='activity'),
]   