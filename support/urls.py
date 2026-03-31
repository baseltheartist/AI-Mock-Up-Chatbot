from django.urls import path
from . import views

app_name = 'support'

urlpatterns = [
    path('chat/', views.ChatView.as_view(), name='chat'),
    path('api/message/', views.MessageAPIView.as_view(), name='api_message'),
]
