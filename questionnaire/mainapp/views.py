from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import render
from django.forms import model_to_dict

from .models import Responder
# from .serializers import ResponderSerializer


class QuestionnaireAPIView(APIView):

	def get(self, request):
		lst = Responder.objects.all().values()
		return Response({'title':list(lst)})

	def post(self, request):
		post_new = Responder.objects.create(
			birth_date=request.data['birth_date'],
			gender=request.data['gender']
		)
		return Response({'post':model_to_dict(post_new)})


# class QuestionnaireAPIView(generics.ListAPIView):
# 	queryset = Responder.objects.all()
# 	serializer_class =  ResponderSerializer