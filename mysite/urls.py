from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="profile"),
    path('login/', views.LoginAPIView.as_view(), name="login"),
    path('logout/', views.logout, name="logout"),
]
