from django.urls import path

from Center_App import views

app_name = '[Center_App]'
urlpatterns = [
    path('homepage/', views.homepage, name='homepage'),
    path('personal_center/', views.personal_center, name='personal_center'),
]























