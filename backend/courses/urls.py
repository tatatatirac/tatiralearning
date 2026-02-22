from django.urls import path
from .views import CourseListView, CourseCreateView, LessonListView, EnrollView


urlpatterns = [

    path('', CourseListView.as_view()),

    path('create/', CourseCreateView.as_view()),

    path('<int:course_id>/lessons/', LessonListView.as_view()),

    path('enroll/', EnrollView.as_view()),
]

from .views import EnrollView