
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/register/', views.UserRegistration.as_view(), name='api_register'),
    path('api/login/', views.UserLogin.as_view(), name='api_login'),
]