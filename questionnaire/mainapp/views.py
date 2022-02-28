import io

from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer
from django.shortcuts import render
from django.forms import model_to_dict

from .models import (
						Responder, PrimaryQuestionBase, PrimaryQuestionAnswer, 
						SubquestionBase, SubquestionPredefinedAnswer, SubquestionAnswer
					)
from .serializers import (
							ResponderSerializer, BasePrimaryQuestionSerializer, 
							AnswerPrimaryQuestionSerializer, BaseSubquestionSerializer,
							AnswerSubquestionPredefinedSerializer, AnswerSubquestionSerializer
						)


class ResponderListAPIView(generics.ListCreateAPIView):

	serializer_class =  ResponderSerializer
	permission_classes = (IsAuthenticated,)
	def get_queryset(self):
		return Responder.objects.filter(interrogator_id=self.request.user)


class BasePrimaryQuestionListAPIView(generics.ListCreateAPIView):
	
	serializer_class =  BasePrimaryQuestionSerializer
	permission_classes = (IsAuthenticated,)
	def get_queryset(self):
		return PrimaryQuestionBase.objects.filter(interrogator_id=self.request.user)


class AnswerPrimaryQuestionListAPIView(generics.ListCreateAPIView):
	
	serializer_class =  AnswerPrimaryQuestionSerializer
	permission_classes = (IsAuthenticated,)
	def get_queryset(self):
		return PrimaryQuestionAnswer.objects.filter(interrogator_id=self.request.user)


class BaseSubquestionListAPIView(generics.ListCreateAPIView):

	serializer_class =  BaseSubquestionSerializer
	permission_classes = (IsAuthenticated,)
	def get_queryset(self):
		queryset = SubquestionBase.objects.filter(interrogator_id=self.request.user)
		return queryset

class AnswerSubquestionPredefinedListAPIView(generics.ListCreateAPIView):
	
	serializer_class =  AnswerSubquestionPredefinedSerializer
	permission_classes = (IsAuthenticated,)
	def get_queryset(self):
		return SubquestionPredefinedAnswer.objects.filter(interrogator_id=self.request.user)

class AnswerSubquestionListAPIView(generics.ListCreateAPIView):
	
	serializer_class =  AnswerSubquestionSerializer
	permission_classes = (IsAuthenticated,)
	def get_queryset(self):
		return SubquestionAnswer.objects.filter(interrogator_id=self.request.user)









# class BaseSubquestionListAPIView(APIView):

# 	def get(self, request):
# 		lst = SubquestionBase.objects.all()
# 		return Response({"a":BaseSubquestionSerializer(lst, many=True).data})

# 	def post(self, request):
# 		print(request.data)

# 		serializer = BaseSubquestionSerializer(data=request.data)
# 		if serializer.is_valid(raise_exception=True):
# 			saved_serializer = serializer.save()

# 		# post_new = Responder.objects.create(
# 		# 	birth_date=request.data['birth_date'],
# 		# 	gender=request.data['gender']
# 		# )
# 		# return Response({'post': ResponderSerializer(post_new).data})
# 		# return Response({saved_serializer})
# 		return Response({'a':'b'})


		# article = request.data.get("article")
  #       # Create an article from the above data
  #       serializer = ArticleSerializer(data=article)
  #       if serializer.is_valid(raise_exception=True):
  #           article_saved = serializer.save()
  #       return Response({"success": "Article '{}' created successfully".format(article_saved.title)})


