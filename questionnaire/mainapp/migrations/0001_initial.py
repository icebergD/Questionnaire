# Generated by Django 4.0.2 on 2022-02-27 17:34

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='SubquestionBase',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.TextField(verbose_name='question')),
                ('interrogator_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='interrogator')),
            ],
        ),
        migrations.CreateModel(
            name='SubquestionPredefinedAnswer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('answer', models.TextField(verbose_name='predefined answer')),
                ('interrogator_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='interrogator')),
                ('subquestion_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainapp.subquestionbase', verbose_name='question')),
            ],
        ),
        migrations.CreateModel(
            name='Responder',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('birth_date', models.DateField(blank=True, null=True, verbose_name='respondrs birth date')),
                ('gender', models.CharField(choices=[('m', 'male'), ('f', 'female'), ('a', 'another')], default='a', max_length=1, verbose_name='gender')),
                ('interrogator_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='interrogator')),
            ],
        ),
        migrations.CreateModel(
            name='PrimaryQuestionBase',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.TextField(verbose_name='question')),
                ('interrogator_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='interrogator')),
            ],
        ),
        migrations.CreateModel(
            name='PrimaryQuestionAnswer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('answer', models.BooleanField(verbose_name='answer to a question (yes/no)')),
                ('interrogator_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='interrogator')),
                ('question_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainapp.primaryquestionbase', verbose_name='question')),
                ('responder_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainapp.responder', verbose_name='responder')),
            ],
        ),
    ]
