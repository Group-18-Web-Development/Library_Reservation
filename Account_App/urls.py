from django.urls import path, re_path

from Account_App import views

app_name = '[Account_App]'
urlpatterns = [
    path('add_data/', views.add_data, name='add_data'),

    path('login/', views.user_login, name="user_login"),
    path('logout/', views.logout, name='logout'),
    path('register/', views.register, name="user_register"),
]
