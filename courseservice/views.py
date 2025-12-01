from rest_framework import viewsets, filters
from django_filters.rest_framework import DjangoFilterBackend
from .models import Course, StudentCourse
from .serializers import CourseSerializer, StudentCourseSerializer

class CourseViewSet(viewsets.ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['name', 'instructor', 'category'] 

class StudentCourseViewSet(viewsets.ModelViewSet):
    queryset = StudentCourse.objects.all()
    serializer_class = StudentCourseSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['student_id', 'course']