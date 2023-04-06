from django.urls import path

from apps.auto_parks.views import AutoParkListCreateView,AutoParksCreateListCarsView


urlpatterns = [
    path('', AutoParkListCreateView.as_view(), name='auto_parks_list_create_view'),
    path('/<int:pk>/cars', AutoParksCreateListCarsView.as_view(), name='auto_parks_car_list_create')
]