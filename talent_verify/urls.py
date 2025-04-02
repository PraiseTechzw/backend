from django.contrib import admin
from django.urls import path, include
from django.http import JsonResponse
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

def welcome(request):
    return JsonResponse({
        "message": "Welcome to Talent Verify API",
        "endpoints": {
            "admin": "/admin/",
            "api": "/api/",
            "token": "/api/auth/token/",
            "token_refresh": "/api/auth/token/refresh/"
        }
    })

urlpatterns = [
    path('', welcome, name='welcome'),
    path('admin/', admin.site.urls),
    path('api/', include('api.urls')),
    path('api/auth/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/auth/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]

