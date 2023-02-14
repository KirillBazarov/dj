from . import views
from django.urls import path

urlpatterns = [
    path('', views.PostList.as_view(), name='home'),
    path('<slug:slug>/', views.PostDetail.as_view(), name='post_detail'),
    # path('register/', views.RegisterUser.as_view(), name='register'),
    # path('login/', views.PostDetail.as_view(), name='login'),
]