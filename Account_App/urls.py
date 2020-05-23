from django.urls import path, re_path
from django.urls import reverse_lazy
from Account_App import views
from django.contrib.auth import views as auth_views
app_name = '[Account_App]'
urlpatterns = [
    path('add_data/', views.add_data, name='add_data'),

    path('login/', views.user_login, name="user_login"),
    path('logout/', views.logout, name='logout'),
    path('register/', views.register, name="user_register"),
    path('password-change/', auth_views.PasswordChangeView.as_view(
        template_name='Account_App/password_change_form.html',
        success_url=reverse_lazy('Account_App:password_change_done')), name='password_change'),
    path('password_change_done/', auth_views.PasswordChangeDoneView.as_view(
        template_name='Account_App/password_change_done.html'), name='password_change_done'),
]
