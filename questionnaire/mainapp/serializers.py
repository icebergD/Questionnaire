from rest_framework import serializers
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser

from .models import Responder


class ResponderSerializer(serializers.ModelSerializer):
	interrogator_id = serializers.HiddenField(default=serializers.CurrentUserDefault())

	class Meta:
		model = Responder
		fields = "__all__"


# class ResponderModel:
# 	def __init__(self, birth_date,gender):
# 		self.birth_date = birth_date
# 		self.gender = gender

# class ResponderSerializer(serializers.Serializer):
# 	birth_date = serializers.DateField()
# 	gender = serializers.CharField(max_length=1)
	
# 	def create(self, validated_data):
# 		return Responder.objects.create(**validated_data)

# def encode():
# 	model = ResponderModel('2000-08-04','a')
# 	model_sr = ResponderSerializer(model)
# 	print(model_sr.data, type(model_sr.data), sep='\n')
# 	json = JSONRenderer().render(model_sr.data)
# 	print(json)

# def decode():
# 	stream = io.BytesIO(b'{"birth_date":"2001-07-07","gender":"m"}')
# 	data = JSONParser().parse(stream)
# 	serializer = ResponderSerializer(data=data)
# 	serializer.is_valid()
# 	print(serializer.validated_data)