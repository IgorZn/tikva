from datetime import datetime
from django.contrib import admin
from django.db import models
from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.contrib.auth import get_user_model

# Create your models here.

# -- MODEL
# Club 1 ......(Subject 1)
# 	Trainer 1 ......(Course 1)
# 		 Group 1 ......(Module 1)
# 			StudentProfile 1 (image, full_name, date_birth, desc, lvl) ......Content 1
# 			StudentProfile 2 (text)
# 	Trainer 2
# 		Group 2
# 			StudentProfile 3 (text)
# 			StudentProfile 4 (file)
# 			StudentProfile 5 (video)

class FullNameManager(models.Manager):
	def get_queryset(self):
		return super().get_user_model()


class User(AbstractUser):
	pass


class Club(models.Model):
	title = models.CharField(max_length=200)
	slug = models.SlugField(max_length=200, unique=True)

	class Meta:
		ordering = ['title']

	def __str__(self):
		return self.title


class Trainer(models.Model):
	name = models.ForeignKey(User, related_name='trainer_created', on_delete=models.CASCADE)
	club = models.ForeignKey(Club, related_name='trainer', on_delete=models.CASCADE)
	description = models.CharField(max_length=200)
	slug = models.SlugField(max_length=200, unique=True)
	overview = models.TextField()
	created = models.DateTimeField(auto_now_add=True)

	class Meta:
		ordering = ['-created']

	def __str__(self):
		return self.name.__str__()


class StudentsGroup(models.Model):
	trainer = models.ForeignKey(Trainer, related_name='students_group', on_delete=models.CASCADE)
	title = models.CharField(max_length=200)
	description = models.TextField(blank=True)

	def __str__(self):
		return self.title


class StudentProfile(models.Model):
	WHITE = 'WHITE'
	WHITE_YELLOW = 'WHITE_YELLOW'
	YELLOW = 'YELLOW'
	YELLOW_GREEN = 'YELLOW_GREEN'
	GREEN = 'GREEN'
	GREEN_BLUE = 'GREEN_BLUE'
	BLUE = 'BLUE'
	BELTS = (
		(WHITE, WHITE),
		(WHITE_YELLOW, WHITE_YELLOW),
		(YELLOW, YELLOW),
		(YELLOW_GREEN, YELLOW_GREEN),
		(GREEN, GREEN),
		(GREEN_BLUE, GREEN_BLUE),
		(BLUE, BLUE),
	)

	def get_full_names(self):
		USERS = get_user_model()
		FNames = [name.get_full_name() for name in USERS.objects.all() if len(name.get_full_name()) > 1]
		return FNames

	FULL_NAMES = tuple(
		zip(
			get_full_names('self'), get_full_names('self')
		)
	)

	user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
	full_name = models.CharField(max_length=90, choices=FULL_NAMES, default='None')
	student_group = models.ForeignKey(StudentsGroup, related_name='group', on_delete=models.CASCADE, null=True)
	trainer = models.ForeignKey(Trainer, related_name='trainer', on_delete=models.CASCADE, null=True)
	photo = models.ImageField(upload_to='photo/%Y/%m/%d', blank=True, null=True)
	name = models.CharField(max_length=200, blank=True, null=True)
	description = models.TextField(blank=True)
	phone = models.CharField(max_length=50, blank=True, null=True)
	email = models.CharField(max_length=50, blank=True, null=True)
	join_date = models.DateTimeField(auto_now_add=True)
	update_date = models.DateTimeField(auto_now=True)
	belt = models.CharField(max_length=20, choices=BELTS, default=WHITE)

	def __str__(self):
		"""
		how it will display at Admin area
		:return:
		"""
		return self.full_name