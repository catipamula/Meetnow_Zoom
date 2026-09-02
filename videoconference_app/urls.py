from django.urls import path
from . import views
<<<<<<< HEAD
from .views import save_recording
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('', views.index, name='index'),
    path('features/', views.features, name='features'),
    path('register/', views.register, name='register'),
    path('login/', views.login_view, name='login'),
    path('contact/', views.contact, name='contact'),
=======

urlpatterns = [
    path('', views.index, name='index'),
    path('register/', views.register, name='register'),
    path('login/', views.login_view, name='login'),
>>>>>>> eb2277fa704e6eef21fa833c13714f22305496f2
    path('dashboard/', views.dashboard, name='dashboard'),
    path('logout/', views.logout_view, name='logout'),
    path('meeting/', views.videocall, name='meeting'),
    path('join_room/', views.join_room, name='join_room'),
    path('random_call/', views.random_call, name='random_call'),
<<<<<<< HEAD
    path('save-recording/', save_recording, name='save_recording'),
    path('forgot-password/', views.forgot_password, name='forgot_password'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(
        template_name='password_reset_confirm.html'
    ), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(
        template_name='password_reset_done.html'
    ), name='password_reset_complete'),
]

=======
]
>>>>>>> eb2277fa704e6eef21fa833c13714f22305496f2
