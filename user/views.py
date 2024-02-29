import os

from django.core.mail import send_mail
from drf_yasg.utils import swagger_auto_schema
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.views import APIView

from root import settings
from .models import UserForm1, UserForm2
from .serializer import UserForm1Serializer, UserForm2Serializer, EmailSerializer


class UserForm1CreateAPIView(generics.ListCreateAPIView):
    queryset = UserForm1.objects.all()
    serializer_class = UserForm1Serializer

    def perform_create(self, serializer):
        instance = serializer.save()
        email = instance.email
        text = 'Sizning ma\'lumotingiz qabul qilindi!'
        try:
            send_mail(
                subject='Ma\'lumot qabuli',
                message=text,
                from_email=os.getenv("EMAIL_HOST_USER"),
                recipient_list=[email],
                fail_silently=False,
            )
            return Response({'message': 'Email sent successfully'}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'error': 'Email don\'t send successfully'}, status=status.HTTP_400_BAD_REQUEST)


class UserForm2CreateAPIView(generics.ListCreateAPIView):
    queryset = UserForm2.objects.all()
    serializer_class = UserForm2Serializer

    def perform_create(self, serializer):
        instance = serializer.save()
        email = instance.email
        text = 'Sizning ma\'lumotingiz qabul qilindi!'
        try:
            send_mail(
                subject='Ma\'lumot qabuli',
                message=text,
                from_email=settings.EMAIL_HOST_USER,
                recipient_list=[email],
                fail_silently=False,
            )
            return Response({'message': 'Email sent successfully'}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'error': 'Email don\'t send successfully'}, status=status.HTTP_400_BAD_REQUEST)


# class SendEmailAPIView(APIView):
#     @swagger_auto_schema(request_body=EmailSerializer)
#     def post(self, request, *args, **kwargs):
#         serializer = EmailSerializer(data=request.data)
#         if serializer.is_valid():
#             email = serializer.validated_data['email']
#             text = serializer.validated_data['text']
#             send_mail(
#                 subject='Message from Your Django App',
#                 message=text,
#                 from_email=os.getenv("EMAIL_HOST_USER"),
#                 recipient_list=[email],
#                 fail_silently=False,
#             )
#             return Response({'message': 'Email sent successfully'}, status=status.HTTP_200_OK)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
