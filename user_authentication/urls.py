from django.urls import path
from django.contrib.auth import views as auth_views
from .forms import MyPasswordResetForm, MySetPasswordForm

from user_authentication import views

urlpatterns = [

    path('user/signup/', views.signup, name='signup'),
    path('user/login/', views.userlogin, name='login'),
    path('user/logout/', views.userlogout, name='logout'),
    path('user/profile/', views.profile, name='profile'),
    path('change_password/', views.change_password_view, name='change_password'),
    path('password-reset/', auth_views.PasswordResetView.as_view(template_name='blog/password_reset.html',form_class=MyPasswordResetForm),name="password_reset"),
    path('password-reset/done/', auth_views.PasswordResetDoneView.as_view(template_name='blog/password_reset_done.html'), name="password_reset_done"),
    path('password-reset-confirm/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='blog/password_reset_confirm.html',form_class=MySetPasswordForm),name="password_reset_confirm"),
    path('password-reset-complate/', auth_views.PasswordResetCompleteView.as_view(template_name='blog/password_reset_complete.html'), name="password_reset_complete"),
]