
from django.contrib import admin
from django.urls import path

from mainapp.views import QuestionnaireAPIView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/responder', QuestionnaireAPIView.as_view())
]
