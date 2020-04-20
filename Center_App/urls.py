from django.urls import path, re_path

from Center_App import views

app_name = '[Center_App]'
urlpatterns = [
    path('/homepage/', views.homepage, name='homepage'),
]























