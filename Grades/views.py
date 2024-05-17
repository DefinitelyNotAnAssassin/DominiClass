from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from Activity.models import Activity, Submission
from Course.models import Course
import json 
# Create your views here.


@csrf_exempt
def grades(request): 
    data = request.POST 
    current_user = data['currentUser']
    # filter all the submissions of the current user and compute the grades per course 
    
    # get all the courses of the current user
    
    # get all the activities of the course
    
    courses = Course.objects.filter(enrolled_students=current_user)
    print(courses)
    
    course_grades = []
    
    for course in courses:
        activities = Activity.objects.filter(course_code=course)
        course_grade = 0
        total_max_grade = 0
        for activity in activities:
            submission = Submission.objects.filter(activity_id=activity, student_id=current_user)
            if submission:
                for sub in submission:
                    course_grade += sub.submission_grade
                    total_max_grade += activity.activity_max_grade
    
        if total_max_grade > 0:
            course_grade_percentage = (course_grade / total_max_grade) * 100
        else:
            course_grade_percentage = 0
    
        course_grades.append({'course': course.course_code, 'course_name' : course.course_name, 'grade': round(course_grade_percentage, 2)})
    
    print(course_grades)
    return JsonResponse({'course_grades': course_grades})
    