from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as DefaultUserAdmin

# Register your models here.
from .models import User, StudentProfile, Club, Trainer, StudentsGroup


@admin.register(User)
class UserAdmin(DefaultUserAdmin):
	pass


@admin.register(StudentProfile)
class TripAdmin(admin.ModelAdmin):
	pass


@admin.register(Club)
class ClubAdmin(admin.ModelAdmin):
	prepopulated_fields = {"slug": ("title",)}


@admin.register(Trainer)
class TrainerAdmin(admin.ModelAdmin):
	prepopulated_fields = {"slug": ("description",)}


@admin.register(StudentsGroup)
class StudentsGroupAdmin(admin.ModelAdmin):
	pass