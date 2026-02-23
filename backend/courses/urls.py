from django.urls import path

from .views import (
    CourseListView,
    CourseCreateView,
    LessonListView,
    EnrollView,
    UploadCourseZipView,
)

urlpatterns = [

    # lista svih kurseva
    path("", CourseListView.as_view()),

    # kreiranje kursa (admin only)
    path("create/", CourseCreateView.as_view()),

    # lekcije za kurs (student ili instructor)
    path("lessons/<int:course_id>/", LessonListView.as_view()),

    # enroll kurs (student)
    path("enroll/", EnrollView.as_view()),

    # upload kompletan kurs ZIP (admin)
    path("upload-zip/", UploadCourseZipView.as_view()),

]