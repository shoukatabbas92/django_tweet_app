from django.urls import path
from . import views
# from django.contrib.auth import views as auth_views
urlpatterns = [
    path('',views.tweet_list,name='tweet_list'),
    path('create/',views.tweet_create,name='tweet_create'),
    path('edit/<int:tweet_id>/', views.tweet_edit, name='tweet_edit'),
    path('delete/<int:tweet_id>/',views.delete_tweet,name='delete_tweet'),
    path('register/',views.register,name='register'),
    #  path('login/', auth_views.LoginView.as_view(), name='login'),
    
]
