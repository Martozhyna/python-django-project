from django.urls import path, include

urlpatterns = [
    path('auto_parks', include('apps.auto_parks.urls')),
    path('auth', include('apps.auth.urls')),
]
