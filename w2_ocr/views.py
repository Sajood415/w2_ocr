from django.contrib.auth import authenticate, login
from rest_framework.authtoken.models import Token
from django.contrib.auth.forms import UserCreationForm
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


class UserRegistration(APIView):
    def post(self, request):
        form = UserCreationForm(request.data)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return Response(status=status.HTTP_201_CREATED)
        return Response(form.errors, status=status.HTTP_400_BAD_REQUEST)

class UserLogin(APIView):
    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')

        user = authenticate(request, username=username, password=password)
        if user is not None:
            token, created = Token.objects.get_or_create(user=user)
            return Response({'token': token.key}, status=status.HTTP_200_OK)
        return Response({'error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)


class ImageUpload(APIView):
    def post(self, request):
        cloudinary_urls = request.data.get('urls')
        # Process the cloudinary_urls, save them to your database, or do other operations
        # Return a response if needed
        return Response({'message': 'Image URLs received and processed'}, status=status.HTTP_200_OK)
