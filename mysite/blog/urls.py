from django.views.decorators.cache import cache_page

from . import views
from django.urls import path

from .views import logout_user

urlpatterns = [
    path('',views.PostList.as_view(), name='home'),
    path('login/', views.LoginUser.as_view(), name='login'),
    path('logout/', logout_user, name='logout'),
    path('feedback/', views.ContactFormView.as_view(), name='feedback'),
    path('register/', views.RegisterUser.as_view(), name='register'),
    path('<slug:slug>/', views.PostDetail.as_view(), name='post_detail'),

]