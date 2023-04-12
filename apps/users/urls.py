from django.urls import path

from .views import (
    AdminBlockView,
    AdminToUserView,
    AdminUnblockView,
    GetAllUsersView,
    UserBlockView,
    UserRetrieveUpdateDestroyView,
    UserToAdminView,
    UserUnblockView,
)

urlpatterns = [
    path('/<int:pk>', UserRetrieveUpdateDestroyView.as_view(), name='users_retrieve_update_destroy'),
    path('/<int:pk>/to_admin', UserToAdminView.as_view(), name='users_to_admin'),
    path('/<int:pk>/to_user', AdminToUserView.as_view(), name='admin_to_user'),
    path('/<int:pk>/block', UserBlockView.as_view(), name='users_block'),
    path('/<int:pk>/unblock', UserUnblockView.as_view(), name='users_unblock'),
    path('/<int:pk>/admin/block', AdminBlockView.as_view(), name='admin_block'),
    path('/<int:pk>/admin/unblock', AdminUnblockView.as_view(), name='admin_unblock'),
    path('/get_all', GetAllUsersView.as_view(), name='users_get_all'),

]
