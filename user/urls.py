from django.urls import path
from .views import UserForm1CreateAPIView, UserForm2CreateAPIView, \
    CategoryNewsListView, NewsListView, TrendingStoriesListView, SpeechAnalysisCreateView

urlpatterns = [
    path('userform1/create/', UserForm1CreateAPIView.as_view(), name='userform1-create'),
    path('userform2/create/', UserForm2CreateAPIView.as_view(), name='userform2-create'),
    path('category-news/', CategoryNewsListView.as_view(), name='category-news-list'),
    path('news/', NewsListView.as_view(), name='news-list'),
    path('trending-stories/', TrendingStoriesListView.as_view(), name='stories-list'),
    path('speech-analysis/', SpeechAnalysisCreateView.as_view(), name='create'),
]
