"""configs URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.urls import path
# from users.views import TestApiView,Test2View
# from users.views import UserListCreateView,UserRetrieveUpdateDestroy
from users.views import UserListCreateView, UserRetrieveUpdateDestroyView

urlpatterns = [
    # path('tests', TestApiView.as_view(), name='user_test'),
    # path('tests/<int:pk>', Test2View.as_view(), name='user_test_pk_view')
    # path('users',UserListCreateView.as_view(), name='users_read_create_view'),
    # path('users/<int:pk>',UserRetrieveUpdateDestroy.as_view(), name='users_retrieve_update_delete_list'),
    path('users', UserListCreateView.as_view(), name='users_create_list_view'),
    path('users/<int:pk>', UserRetrieveUpdateDestroyView.as_view(), name='users_retrieve_update_delete_view')

]
