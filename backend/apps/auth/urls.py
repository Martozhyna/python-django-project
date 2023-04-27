from django.urls import path

from rest_framework_simplejwt.views import TokenRefreshView

from .views import ActivateUserView, AuthRegisterView, PasswordChangeView, PasswordRecoveryView, TokenPairView

urlpatterns = [
    path('', TokenPairView.as_view(), name='auth_login'),
    path('/refresh', TokenRefreshView.as_view(), name='auth_refresh'),
    path('/register', AuthRegisterView.as_view(), name='auth_register'),
    path('/activate/<str:token>', ActivateUserView.as_view(), name='auth_user_activate'),
    path('/recovery/password', PasswordRecoveryView.as_view(), name='auth_user_recovery_password'),
    path('/change/password/<str:token>', PasswordChangeView.as_view(), name='auth_user_change_password')
]