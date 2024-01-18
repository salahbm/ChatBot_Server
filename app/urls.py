from django.urls import path
from . import views

# Init

urlpatterns = [
    path('', views.index),
    path('storeUser/', views.store_user, name='store_user'),
    path('getUserById/', views.get_user_by_id)
]
