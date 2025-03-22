from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    ROLE_CHOICES = (
        ('admin', 'Admin'),
        ('student', 'Student'),
    )

    ORGANIZATION_CHOICES = (
        ('ktu', 'KTU'),
        ('abc school', 'ABC SCHOOL'),
        ('mg university ', 'MG UNIVERSITY'),
        ('kode club', 'KODE CLUB'),

    )

    email = models.EmailField(unique=True)
    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default='student')
    phone_number = models.CharField(max_length=15, unique=True, blank=True, null=True)
    profile_picture = models.ImageField(upload_to='profile_pics/', blank=True, null=True)
    address = models.TextField(blank=True, null=True)
    date_of_birth = models.DateField(null=True, blank=True)
    organization = models.CharField(max_length=225, choices=ORGANIZATION_CHOICES, default='ktu')



    def __str__(self):
        return f"{self.username}"

