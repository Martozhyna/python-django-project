from django.urls import path
from .views import AutoParkListCreateView,AutoParkCreateListCarsView

urlpatterns = [
    path('', AutoParkListCreateView.as_view(), name='auto_park_list_create'),
    path('/<int:pk>/cars', AutoParkCreateListCarsView.as_view(), name='auto_park_cars_list_create')
]