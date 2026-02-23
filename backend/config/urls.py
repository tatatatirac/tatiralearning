from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [

    # Admin panel
    path("admin/", admin.site.urls),

    # Users (register, profile, etc.)
    path("api/users/", include("users.urls")),

    # Courses endpoints
    path("api/courses/", include("courses.urls")),

    # JWT Login + token refresh
    path("api/login/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("api/token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),

]