from django.db import models
from django.contrib.auth import get_user_model

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

	birth_date = models.DateField(verbose_name='respondrs birth date')
	gender = models.CharField(
		max_length=1, 
		verbose_name='gender',
		choices=GENDER,
		default=ANOTHER
	)

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
	answer = models.BooleanField(verbose_name='answer to a question')
	def __str__(self):
		return 'Answer: {}'.format(self.answer)


class SubquestionBase(models.Model):

	question = models.TextField(verbose_name='question')
	predefined_answer = models.TextField(verbose_name='predefined answer', null=True, blank=True)
	interrogator_id = models.ForeignKey(User, verbose_name='interrogator', on_delete=models.CASCADE)

	def __str__(self):
		return 'Question: {}'.format(self.question)


class SubquestionAnswer(models.Model):

	responder_id = models.ForeignKey(Responder, verbose_name='responder', on_delete=models.CASCADE)
	question_id =  models.ForeignKey(SubquestionBase, verbose_name='question', on_delete=models.CASCADE)
	answer = models.TextField(verbose_name='answer')

	def __str__(self):
		return 'Answer: {}'.format(self.answer)


