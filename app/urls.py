from django.urls import path
from app.views import userResponse, ChatbotStepListCreateView , index

# Init

urlpatterns = [
    path('', index, name='index'),
    path('userResponse/',userResponse.as_view(),name='user_api_view'),
    path('chatbotSteps/', ChatbotStepListCreateView.as_view(), name='chatbot_steps_api_view'),
]
