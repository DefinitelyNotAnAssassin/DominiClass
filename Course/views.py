from django.shortcuts import render
from django.http import JsonResponse
from django.core import serializers
from django.views.decorators.csrf import csrf_exempt
from Course.models import Course, CourseMaterial
from Activity.models import Activity, Submission
from UserAuthentication.models import Account


# Create your views here.


def course(request, course_code):
    return render(request, 'Course/course.html')

def course_material(request, course_code):
    return render(request, 'Course/course_material.html')

def course_activity(request, course_code):
    return render(request, 'Course/course_activity.html')

def activity(request, course_code, activity_id):
    
    return render(request, 'Course/activity.html')


def submission(request, course_code, activity_id, submission_id):
    return render(request, 'Course/submission.html')

@csrf_exempt
def enroll(request):
    data = request.POST
    print(data)
    try:
        
        # course_code 
        
        # SELECT * FROM Course WHERE course_code = data['course_code']
        
        # IT101
        
        # Object Relational Mapping (ORM)
        Course.objects.get(course_code=data['course_code']).enrolled_students.add(data['currentUser'])
        return JsonResponse({'message': 'Enrollment successful'})   
    except Exception as e:
        print(e)
        return JsonResponse({'message': 'Course does not exist'})
    
    
    
    
@csrf_exempt
def getCourse(request):
    data = request.POST  
    course = Course.objects.filter(enrolled_students=data['currentUser']).values()
    print(course)
    return JsonResponse({'course': list(course)})
    
    



@csrf_exempt    
def getExactCourse(request, course_id):
    course = Course.objects.get(id=course_id)
    course_materials = CourseMaterial.objects.filter(course_code_id=course)
    activities = Activity.objects.filte
    
    return JsonResponse({
     
            'course_code': course.course_code,
            'course_description': course.course_description,
            'course_materials': list(course_materials.values()),
            'activities': list(activities.values())
        
    })
    
    
def lesson(request, lesson_id):
    # SELECT * FROM CourseMaterial WHERE id = lesson_id 
    lesson = CourseMaterial.objects.get(id=lesson_id)
    return JsonResponse({"material_name": lesson.material_name, "material_description": lesson.material_description, "course_code": lesson.course_code.course_code, "course_name": lesson.course_code.course_name, "course_description": lesson.course_code.course_description})


def exact_activity(request, activity_id):
    activity = Activity.objects.get(id=activity_id)
    return JsonResponse({"activity_name": activity.activity_name, "activity_description": activity.activity_description, "course_code": activity.course_code.course_code, "course_name": activity.course_code.course_name})


@csrf_exempt    
def submit_activity(request, activity_id):
    data = request.POST
    activity = Activity.objects.get(id=activity_id)
    isExisting = Submission.objects.filter(activity_id=activity, student_id=Account.objects.get(id = data['currentUser']))
    if isExisting:
        return JsonResponse({"message": "Submission already exists"})
    else:
        submission = Submission(activity_id=activity, student_id=Account.objects.get(id = data['currentUser']), submission_grade=None, answer=data['formData'])
        submission.save()
        return JsonResponse({"message": "Submission successful"})
    
    
@csrf_exempt    
def getMissingActivities(request):
    data = request.POST
    # get the courses of the current user and store all of the missing activities 
    
    courses = Course.objects.filter(enrolled_students=data['currentUser'])
    missing_activities = []
    for course in courses:
        activities = Activity.objects.filter(course_code=course)
        for activity in activities:
            submission = Submission.objects.filter(activity_id=activity, student_id=data['currentUser'])
            if not submission:
                missing_activities.append({'activity_name': activity.activity_name, 'course_name': course.course_name})
                
    return JsonResponse({'missing_activities': missing_activities})

@csrf_exempt
def getFinishedActivities(request):
    data = request.POST
    # get the courses of the current user and store all of the missing activities 
    
    courses = Course.objects.filter(enrolled_students=data['currentUser'])
    finished_activities = []
    for course in courses:
        activities = Activity.objects.filter(course_code=course)
        for activity in activities:
            submission = Submission.objects.filter(activity_id=activity, student_id=data['currentUser'])
            if submission:
                finished_activities.append({'activity_name': activity.activity_name, 'course_name': course.course_name})
                
    return JsonResponse({'finished_activities': finished_activities})