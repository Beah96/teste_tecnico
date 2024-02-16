from django.urls import path
from .views import UserCreateView
from rest_framework_simplejwt import views as jwt_views

urlpatterns = [
    path('users/', UserCreateView.as_view()),
    path('users/login/', jwt_views.TokenObtainPairView.as_view())
]