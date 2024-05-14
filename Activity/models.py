from django.db import models

# Create your models here.

class Activity(models.Model):
    activity_name = models.CharField(max_length=100)
    activity_description = models.TextField()
    activity_date = models.DateField()
    activity_time = models.TimeField()
    course_code = models.ForeignKey('Course.Course', on_delete=models.CASCADE)
    activity_max_grade = models.FloatField()
    
    def __str__(self):
        return self.activity_name
    
    
class Submission(models.Model):
    activity_id = models.ForeignKey('Activity.Activity', on_delete=models.CASCADE)
    student_id = models.ForeignKey('UserAuthentication.Account', on_delete=models.CASCADE)
    submission_grade = models.FloatField(null=True, blank=True)

    
    def __str__(self):
        return self.activity_id.activity_name + ' - ' + self.student_id.username