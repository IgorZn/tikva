from datetime import datetime
from django.db import models
from django.conf import settings
from django.contrib.auth.models import AbstractUser

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
	course = models.ForeignKey(Trainer, related_name='students_group', on_delete=models.CASCADE)
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

	user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
	photo = models.ImageField(upload_to='photo/%Y/%m/%d')
	name = models.CharField(max_length=200)
	description = models.TextField(blank=True)
	phone = models.CharField(max_length=50)
	email = models.CharField(max_length=50)
	join_date = models.DateTimeField(auto_now_add=True)
	update_date = models.DateTimeField(auto_now=True)
	belt = models.CharField(max_length=20, choices=BELTS, default=WHITE)

	def __str__(self):
		"""
		how it will display at Admin area
		:return:
		"""
		return self.name