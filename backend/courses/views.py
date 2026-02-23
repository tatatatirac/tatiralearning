from rest_framework import generics, permissions
from .models import Course
from .serializers import CourseSerializer
from .models import Course, Lesson, Enrollment
from .serializers import CourseSerializer, LessonSerializer, EnrollmentSerializer
from rest_framework.exceptions import PermissionDenied
from .models import Course, Lesson, Enrollment
from rest_framework.permissions import IsAuthenticated
from rest_framework.exceptions import PermissionDenied
import zipfile
import json
from django.core.files.base import ContentFile
from .models import ExternalCourseUpload, Course, Lesson

from rest_framework.parsers import MultiPartParser
from rest_framework.response import Response
from rest_framework import status, permissions
from .serializers import ExternalCourseUploadSerializer

from .serializers import (
    CourseSerializer,
    ExternalCourseUploadSerializer,   # <--- ovaj mora biti tu
    LessonSerializer
)

class CourseListView(generics.ListAPIView):

    queryset = Course.objects.all()

    serializer_class = CourseSerializer


class CourseCreateView(generics.CreateAPIView):

    serializer_class = CourseSerializer

    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):

        if not self.request.user.is_staff and not self.request.user.is_superuser:
            raise PermissionDenied("Only admin can create courses.")

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




class UploadCourseZipView(generics.CreateAPIView):

    parser_classes = [MultiPartParser]
    permission_classes = [permissions.IsAdminUser]  # samo admin može uploadovati
    serializer_class = ExternalCourseUploadSerializer

    def post(self, request, *args, **kwargs):

        if "file" not in request.FILES:
            return Response({"error": "No file provided"}, status=status.HTTP_400_BAD_REQUEST)

        zip_file = request.FILES["file"]

        if not zipfile.is_zipfile(zip_file):
            return Response({"error": "Not a valid zip file"}, status=status.HTTP_400_BAD_REQUEST)

        # Sačuvaj upload za evidenciju
        upload_obj = ExternalCourseUpload(file=zip_file)
        upload_obj.save()

        # Parsiraj ZIP
        z = zipfile.ZipFile(zip_file)

        # PROCITAJ course.json
        try:
            raw = z.read("course.json")
        except KeyError:
            return Response({"error": "course.json not found in zip"}, status=status.HTTP_400_BAD_REQUEST)

        data = json.loads(raw)

        # Kreiraj Course
        course = Course.objects.create(
            instructor=request.user,
            title=data.get("title", ""),
            description=data.get("description", ""),
            price=data.get("price", 0),
            status="draft"  # po defaultu ide draft
        )

        # Thumbnail
        if "thumbnail.jpg" in z.namelist():
            thumb_data = z.read("thumbnail.jpg")
            course.thumbnail.save("thumbnail.jpg", ContentFile(thumb_data), save=True)

        # Kreiraj Lessons
        for lesson_info in data.get("lessons", []):
            video_path = lesson_info.get("video")
            lesson_title = lesson_info.get("title", "")

            lesson_obj = Lesson(course=course, title=lesson_title)

            if video_path in z.namelist():
                video_data = z.read(video_path)
                lesson_obj.video.save(video_path.split("/")[-1], ContentFile(video_data), save=True)

            lesson_obj.save()

        # Dodatni fajlovi (resursi)
        # Možeš dodati model CourseFile ako želiš, ja ću to uraditi u sledećem koraku.

        return Response({
            "message": "Course uploaded successfully",
            "course_id": course.id,
            "course_title": course.title,
            "status": course.status,
        })
    
    