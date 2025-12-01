from django.db import models

class Course(models.Model):
    name = models.CharField(max_length=255)
    instructor = models.CharField(max_length=255)
    category = models.CharField(max_length=100)
    schedule = models.TextField() 

    def __str__(self):
        return self.name

class StudentCourse(models.Model):
    student_id = models.IntegerField() 
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='enrollments')
    class Meta:
        unique_together = ('student_id', 'course') 
    def __str__(self):
        return f"Student {self.student_id} in Course {self.course.name}"