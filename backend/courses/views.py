from rest_framework import generics, permissions
from .models import Course
from .serializers import CourseSerializer
from .models import Course, Lesson, Enrollment
from .serializers import CourseSerializer, LessonSerializer, EnrollmentSerializer
from rest_framework.exceptions import PermissionDenied
from .models import Course, Lesson, Enrollment


class CourseListView(generics.ListAPIView):

    queryset = Course.objects.all()

    serializer_class = CourseSerializer


class CourseCreateView(generics.CreateAPIView):

    queryset = Course.objects.all()

    serializer_class = CourseSerializer

    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):

        serializer.save(instructor=self.request.user)

from rest_framework.exceptions import PermissionDenied


class LessonListView(generics.ListAPIView):

    serializer_class = LessonSerializer

    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):

        course_id = self.kwargs['course_id']

        user = self.request.user

        is_enrolled = Enrollment.objects.filter(
            student=user,
            course_id=course_id
        ).exists()

        is_instructor = Course.objects.filter(
            id=course_id,
            instructor=user
        ).exists()

        if not is_enrolled and not is_instructor:

            raise PermissionDenied("You are not enrolled in this course.")

        return Lesson.objects.filter(course_id=course_id)
    
class EnrollView(generics.CreateAPIView):

    serializer_class = EnrollmentSerializer

    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):

        serializer.save(student=self.request.user)

def perform_create(self, serializer):

        serializer.save(student=self.request.user)