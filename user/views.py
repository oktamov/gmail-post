import os
from email.mime.multipart import MIMEMultipart

from django.template.loader import render_to_string
from rest_framework import generics, status
from rest_framework.response import Response

from gmail_html import HTML
from root import settings
from .models import UserForm1, UserForm2, CategoryNews, News, TrendingStories
from .pagination import CustomPagination
from .serializer import UserForm1Serializer, UserForm2Serializer, CategoryNewsSerializer, NewsSerializer, \
    TrendingStoriesSerializer

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


class NewsListView(generics.ListAPIView):
    serializer_class = NewsSerializer
    pagination_class = CustomPagination

    def get_queryset(self):
        """
        Optionally filters the news by 'status' parameter in the URL.
        """
        queryset = News.objects.all()
        status = self.request.query_params.get('status', None)
        if status is not None:
            queryset = queryset.filter(status=status)
        return queryset


class TrendingStoriesListView(generics.ListAPIView):
    queryset = TrendingStories.objects.order_by('-id')
    serializer_class = TrendingStoriesSerializer
