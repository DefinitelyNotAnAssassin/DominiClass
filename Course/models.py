from django.db import models



class Course(models.Model):
    course_code = models.CharField(max_length=100)
    course_name = models.CharField(max_length=100)
    course_description = models.TextField() 
    enrolled_students = models.ManyToManyField('UserAuthentication.Account', related_name='enrolled_students')
    
    
    def __str__(self):
        return self.course_code + ' - ' + self.course_name
    
    
    
class CourseMaterial(models.Model):
    course_code = models.ForeignKey('Course.Course', on_delete=models.CASCADE)
    material_name = models.CharField(max_length=100)
    material_description = models.TextField()
    
    def __str__(self):
        return self.material_name