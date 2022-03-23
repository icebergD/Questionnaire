
from django.contrib import admin
from django.urls import path, include, re_path

from mainapp.views import (
								homePageView,
								ResponderListAPIView, BasePrimaryQuestionListAPIView, 
								AnswerPrimaryQuestionListAPIView, BaseSubquestionListAPIView,
								AnswerSubquestionPredefinedListAPIView, AnswerSubquestionListAPIView
							)
from .yasg import urlpatterns as doc_urls

urlpatterns = [

	path("", homePageView),
	path('admin/', admin.site.urls),
	path('api/v1/responder/', ResponderListAPIView.as_view()),
	path('api/v1/BasePrimaryQuestion/', BasePrimaryQuestionListAPIView.as_view()),
	path('api/v1/AnswerPrimaryQuestion/', AnswerPrimaryQuestionListAPIView.as_view()),
	path('api/v1/BaseSubquestion/', BaseSubquestionListAPIView.as_view()),
	path('api/v1/AnswerSubquestionPredefined/', AnswerSubquestionPredefinedListAPIView.as_view()),
	path('api/v1/AnswerSubquestion/', AnswerSubquestionListAPIView.as_view()),

	path('api/v1/auth/', include('djoser.urls')),
	re_path(r'^auth/', include('djoser.urls.authtoken')),
]

urlpatterns += doc_urls
