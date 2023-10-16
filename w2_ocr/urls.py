from django.contrib import admin
from django.urls import path
from .views import UserRegistration, UserLogin, ImageUpload

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/register/', UserRegistration.as_view(), name='api_register'),
    path('api/login/', UserLogin.as_view(), name='api_login'),
    path('api/image-upload/', ImageUpload.as_view(), name='api_image_upload'),

]
