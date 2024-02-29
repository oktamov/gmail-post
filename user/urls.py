from django.urls import path
from .views import UserForm1CreateAPIView, UserForm2CreateAPIView

urlpatterns = [
    path('userform1/create/', UserForm1CreateAPIView.as_view(), name='userform1-create'),
    path('userform2/create/', UserForm2CreateAPIView.as_view(), name='userform2-create'),
    # path('send-email/', SendEmailAPIView.as_view(), name='send-email'),

]

