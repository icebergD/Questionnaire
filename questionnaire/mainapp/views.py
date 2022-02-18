from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from django.shortcuts import render
from django.forms import model_to_dict

from .models import Responder
from .serializers import ResponderSerializer


class ResponderListAPIView(generics.ListCreateAPIView):
	queryset = Responder.objects.all()
	serializer_class =  ResponderSerializer
	permission_classes = (IsAuthenticatedOrReadOnly,)


# class QuestionnaireAPIView(APIView):

# 	def get(self, request):
# 		lst = Responder.objects.all()
# 		return Response({'title': ResponderSerializer(lst, many=True).data})

# 	def post(self, request):
# 		serializer = ResponderSerializer(data=request.data)
# 		serializer.is_valid(raise_exception=True)
# 		serializer.save()

# 		# post_new = Responder.objects.create(
# 		# 	birth_date=request.data['birth_date'],
# 		# 	gender=request.data['gender']
# 		# )
# 		# return Response({'post': ResponderSerializer(post_new).data})
# 		return Response({'post': serializer.data})


