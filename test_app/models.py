from django.db import models
from student.models import Organization

# Create your models here.
class Subject(models.Model):
    name = models.CharField(max_length=255)
    organization = models.ForeignKey(Organization, on_delete=models.CASCADE)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.subject_name




class Chapter(models.Model):
    name = models.CharField(max_length=255)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    title = models.CharField(max_length=200,null=False)

    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name




class Question(models.Model):

    chapter = models.ForeignKey(Chapter, on_delete=models.CASCADE)
    question_no = models.IntegerField()
    question_text = models.TextField()
    option_a = models.CharField(max_length=255)
    option_b = models.CharField(max_length=255)
    option_c = models.CharField(max_length=255)
    option_d = models.CharField(max_length=255)
    correct_option = models.CharField(max_length=1, choices=[
        ('A', 'Option A'),
        ('B', 'Option B'),
        ('C', 'Option C'),
        ('D', 'Option D'),
    ])
    year = models.IntegerField(null=True)
    answer = models.CharField(null=True)
    explanation = models.CharField(null=True)
    verified = models.BooleanField(null=False)
    organization_id =models.ForeignKey(Organization, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.question_no


















