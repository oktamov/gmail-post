import os

from django.core.mail import send_mail
from drf_yasg.utils import swagger_auto_schema
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import UserForm1, UserForm2
from .serializer import UserForm1Serializer, UserForm2Serializer, EmailSerializer


class UserForm1CreateAPIView(generics.CreateAPIView):
    queryset = UserForm1.objects.all()
    serializer_class = UserForm1Serializer


class UserForm2CreateAPIView(generics.CreateAPIView):
    queryset = UserForm2.objects.all()
    serializer_class = UserForm2Serializer


class SendEmailAPIView(APIView):
    @swagger_auto_schema(request_body=EmailSerializer)
    def post(self, request, *args, **kwargs):
        serializer = EmailSerializer(data=request.data)
        if serializer.is_valid():
            email = serializer.validated_data['email']
            text = serializer.validated_data['text']
            send_mail(
                subject='Message from Your Django App',
                message=text,
                from_email=os.getenv("EMAIL_HOST_USER"),
                recipient_list=[email],
                fail_silently=False,
            )
            return Response({'message': 'Email sent successfully'}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
