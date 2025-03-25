from django.db import models
from authentication.models import CustomUser
from django.conf import settings



class Organization(models.Model):

    name = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    country = models.CharField(max_length=200)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f"organization: {self.name}"



class StudentProfile(models.Model):

    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='student_profile', default=True)
    date_of_birth = models.DateField(null=True, blank=True)
    phone_number = models.CharField(max_length=15, null=True, blank=True)
    address = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.user.username



class Course(models.Model):

    course_name = models.CharField(max_length=225)
    organization = models.ForeignKey(Organization, on_delete=models.SET_NULL, null=True, blank=True)
    description = models.CharField(max_length=225)
    is_active = models.BooleanField(default=True)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.course_name

