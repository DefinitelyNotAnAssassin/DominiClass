from django.db import models



class Course(models.Model):
    course_code = models.CharField(max_length=100)
    course_name = models.CharField(max_length=100)
    course_description = models.TextField() 
    enrolled_students = models.ManyToManyField('UserAuthentication.Account', related_name='enrolled_students')
    