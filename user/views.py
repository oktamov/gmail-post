import os
from email.mime.multipart import MIMEMultipart

from django.template.loader import render_to_string
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from rest_framework import generics, status
from rest_framework.response import Response

from gmail_html import HTML
from root import settings
from .models import UserForm1, UserForm2, CategoryNews, News, TrendingStories, SpeechAnalysis
from .pagination import CustomLimitOffsetPagination
from .send_telegram import send_order_notification
from .serializer import UserForm1Serializer, UserForm2Serializer, CategoryNewsSerializer, NewsSerializer, \
    TrendingStoriesSerializer, SpeechAnalysisSerializer

from email.mime.text import MIMEText
from smtplib import SMTP_SSL


def email_send_html(html, to_email):
    my_email = settings.EMAIL_HOST_USER
    password = settings.EMAIL_HOST_PASSWORD
    msg = MIMEMultipart()
    msg['Subject'] = f'Nikel token'
    msg['From'] = my_email

    msg.attach(MIMEText(render_to_string('index.html'), 'html'))

    with SMTP_SSL('smtp.gmail.com', 465) as smtp:
        smtp.login(my_email, password)
        smtp.sendmail(my_email, to_email, msg.as_string())


class UserForm1CreateAPIView(generics.ListCreateAPIView):
    queryset = UserForm1.objects.all()
    serializer_class = UserForm1Serializer

    def perform_create(self, serializer):
        instance = serializer.save()
        email = instance.email
        try:
            email_send_html(HTML, email)
            return Response({'message': 'Email sent successfully'}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'error': 'Email don\'t send '}, status=status.HTTP_400_BAD_REQUEST)


class UserForm2CreateAPIView(generics.ListCreateAPIView):
    queryset = UserForm2.objects.all()
    serializer_class = UserForm2Serializer

    def perform_create(self, serializer):
        instance = serializer.save()
        email = instance.email
        try:
            email_send_html(HTML, email)
            return Response({'message': 'Email sent successfully'}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'error': 'Email don\'t send successfully'}, status=status.HTTP_400_BAD_REQUEST)


class CategoryNewsListView(generics.ListAPIView):
    queryset = CategoryNews.objects.all()
    serializer_class = CategoryNewsSerializer


class NewsListView(generics.GenericAPIView):
    serializer_class = NewsSerializer
    pagination_class = CustomLimitOffsetPagination

    def get_queryset(self):
        queryset = News.objects.all()
        status = self.request.query_params.get('status', None)
        if status is not None:
            queryset = queryset.filter(status=status)
        return queryset

    @swagger_auto_schema(
        manual_parameters=[
            openapi.Parameter(
                name="status",
                in_=openapi.IN_QUERY,
                type=openapi.TYPE_STRING,
                description=News.STATUS_CHOICES,
            ),
        ]
    )
    def get(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)


class NewsDetailView(generics.RetrieveAPIView):
    queryset = News.objects.all()
    serializer_class = NewsSerializer


class TrendingStoriesListView(generics.ListAPIView):
    queryset = TrendingStories.objects.order_by('-id')
    serializer_class = TrendingStoriesSerializer
    pagination_class = CustomLimitOffsetPagination


class SpeechAnalysisCreateView(generics.CreateAPIView):
    queryset = SpeechAnalysis.objects.all()
    serializer_class = SpeechAnalysisSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        full_name = serializer.validated_data['full_name']
        company_name = serializer.validated_data['company_name']
        email = serializer.validated_data['email']
        send_order_notification(full_name, company_name, email)
        queryset = SpeechAnalysis.objects.create(full_name=full_name, company_name=company_name, email=email)
        return Response({'detail: Successfully created'}, status=status.HTTP_201_CREATED)
