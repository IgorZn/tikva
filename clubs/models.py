from datetime import datetime
from django.db import models
from django.conf import settings
from django.contrib.auth.models import AbstractUser

# Create your models here.

# MODEL
# Club 1
# 	Trainer 1
# 		 Group 1
# 			Student 1 (image, full_name, date_birth, desc, lvl)
# 			Student 2 (text)
# 	Trainer 2
# 		Group 2
# 			Student 3 (text)
# 			Student 4 (file)
# 			Student 5 (video)


class User(AbstractUser):
	pass


class Profile(models.Model):
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