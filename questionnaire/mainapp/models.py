from django.db import models

class Responder(models.Model):
	birth_date = 
	gender = 

class PrimaryQuestionBase(models.Model):
	question = models.TextField()
	interrogator_id =

class PrimaryQuestionAnswer(models.Model):
	responder_id = 
	question_id = 
	answer = models.BooleanField(verbose_name='answer to a question')


class SubquestionBase(models.Model):
	question = models.TextField()
	q_type =
	answer =
	interrogator_id =

class SubquestionAnswer(models.Model):
	responder_id =
	question_id = 
	answer = 

