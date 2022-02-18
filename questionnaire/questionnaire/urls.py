
from django.contrib import admin
from django.urls import path

from mainapp.views import ResponderListAPIView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/responder', ResponderListAPIView.as_view())
]
