from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('booking.urls')),
    path('api/token/', include('rest_framework_simplejwt.urls')),
]
