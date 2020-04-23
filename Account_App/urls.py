from django.urls import path, re_path

from Account_App import views

app_name = '[Account_App]'
urlpatterns = [
    path('test/', views.test, name='test'),
    path('login/', views.user_login, name="user_login"),
    path('logout/', views.logout, name='logout')
]
