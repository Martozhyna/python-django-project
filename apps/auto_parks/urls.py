from django.urls import path

from apps.auto_parks.views import AutoParkListCreateView,AutoParkCarsListCreateView

urlpatterns = [
    path('', AutoParkListCreateView.as_view(), name='auto_parks_list_create'),
    path('/<int:pk>/cars', AutoParkCarsListCreateView.as_view(), name='auto_parks_cars_create')

]