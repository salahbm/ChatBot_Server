from django.urls import path
from app.views import UserAPIView , index

# Init

urlpatterns = [
    path('', index, name='index'),
    path('UserAPIView/',UserAPIView.as_view(),name='user_api_view'),
]
