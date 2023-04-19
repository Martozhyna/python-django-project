from django.urls import path

from apps.cars.views import CarAddPhotosView, CarListCreateView, CarPhotoDeleteView, CarRetrieveUpdateDestroyView

urlpatterns = [
    path('', CarListCreateView.as_view(), name='cars_list_create'),
    path('/<int:pk>', CarRetrieveUpdateDestroyView.as_view(), name='cars_retrieve_update_destroy'),
    path('/<int:pk>/photo', CarAddPhotosView.as_view(), name='cars_add_photo'),
    path('/photo/<int:pk>', CarPhotoDeleteView.as_view(), name='cars_photo_delete')

]
