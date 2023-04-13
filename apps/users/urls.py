from django.urls import path

from .views import UserToAdminView

urlpatterns = [
    path('/<int:pk>/to_admin', UserToAdminView.as_view(), name='users_to_admin'),

]
