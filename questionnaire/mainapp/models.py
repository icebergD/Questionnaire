from django.db import models
from django.contrib.auth import get_user_model
from django.db.models import DEFERRED

from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer
import io

User = get_user_model()


class Responder(models.Model):

	MALE = 'm'
	FEMALE = 'f'
	ANOTHER = 'a'

	GENDER = (
        (MALE, 'male'),
        (FEMALE, 'female'),
        (ANOTHER, 'another'),
    )

	birth_date = models.DateField(verbose_name='respondrs birth date', null=True, blank=True)
	gender = models.CharField(
		max_length=1, 
		verbose_name='gender',
		choices=GENDER,
		default=ANOTHER
	)
	interrogator_id = models.ForeignKey(User, verbose_name='interrogator', on_delete=models.CASCADE)
	def __str__(self):
		return 'Responder: {} , {}'.format(self.birth_date, self.gender)


class PrimaryQuestionBase(models.Model):

	question = models.TextField(verbose_name='question')
	interrogator_id = models.ForeignKey(User, verbose_name='interrogator', on_delete=models.CASCADE)

	def __str__(self):
		return 'Question: {}'.format(self.question)


class PrimaryQuestionAnswer(models.Model):

	responder_id =  models.ForeignKey(Responder, verbose_name='responder', on_delete=models.CASCADE)
	question_id =  models.ForeignKey(PrimaryQuestionBase, verbose_name='question', on_delete=models.CASCADE)
	answer = models.BooleanField(verbose_name='answer to a question (yes/no)')
	interrogator_id = models.ForeignKey(User, verbose_name='interrogator', on_delete=models.CASCADE)
	def __str__(self):
		return 'Answer: {}'.format(self.answer)


class SubquestionBase(models.Model):
	primary_question = models.ForeignKey(PrimaryQuestionBase, verbose_name='primary question id', on_delete=models.CASCADE)
	question = models.TextField(verbose_name='question')
	interrogator_id = models.ForeignKey(User, verbose_name='interrogator', on_delete=models.CASCADE)

	def __str__(self):
		return 'Question: {}'.format(self.question)

class SubquestionPredefinedAnswer(models.Model):
	subquestion_id = models.ForeignKey(SubquestionBase, verbose_name='question', on_delete=models.CASCADE)
	answer = models.TextField(verbose_name='predefined answer')
	interrogator_id = models.ForeignKey(User, verbose_name='interrogator', on_delete=models.CASCADE)
	
	def __str__(self):
		return 'Predefind answer : {} / to question : {}'.format(self.answer,self.subquestion_id)


class SubquestionAnswer(models.Model):

	responder_id = models.ForeignKey(Responder, verbose_name='responder', on_delete=models.CASCADE)
	question_id =  models.ForeignKey(SubquestionBase, verbose_name='question', on_delete=models.CASCADE)
	answer = models.TextField(verbose_name='answer')
	interrogator_id = models.ForeignKey(User, verbose_name='interrogator', on_delete=models.CASCADE)

	def __str__(self):
		return 'Answer : {} / to question : {}'.format(self.answer, self.question_id)
