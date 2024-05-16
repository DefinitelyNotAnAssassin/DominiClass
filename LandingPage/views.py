from django.shortcuts import render
from Course.models import Course
# Create your views here.


def index(request):
    data = Course.objects.get(course_code='IT101')
    print(data.activity_set.all())
    
    
    
    
    
    # SELECT * FROM Course JOIN Activity ON Course.course_code = Activity.course_code WHERE Course.course_code = 'IT101'
    return render(request, 'LandingPage/index.html')