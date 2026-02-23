from rest_framework import serializers
from .models import Course, Lesson, Enrollment, ExternalCourseUpload


class CourseSerializer(serializers.ModelSerializer):
    instructor_name = serializers.CharField(source="instructor.username", read_only=True)

    class Meta:
        model = Course
        fields = "__all__"
        read_only_fields = ["instructor", "created_at"]


class LessonSerializer(serializers.ModelSerializer):

    class Meta:
        model = Lesson
        fields = "__all__"


class EnrollmentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Enrollment
        fields = "__all__"


class ExternalCourseUploadSerializer(serializers.ModelSerializer):

    class Meta:
        model = ExternalCourseUpload
        fields = ["id", "file", "uploaded_at"]