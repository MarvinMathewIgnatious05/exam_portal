from django.db import models
from student.models import Organization
from django.conf import settings

# Create your models here.



class Subject(models.Model):

    subject_name = models.CharField(max_length=255)
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
    answer = models.CharField(max_length=255, default="Default Answer")
    explanation = models.CharField(max_length=500, default="No explanation provided.")
    verified = models.BooleanField(null=False)
    organization_id =models.ForeignKey(Organization, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return str(self.question_no)






class MockTest(models.Model):
    student = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="mock_tests")
    score = models.FloatField(default=0)
    completed = models.BooleanField(default=False)
    organization_id =models.ForeignKey(Organization, on_delete=models.SET_NULL, null=True, blank=True)


    def __str__(self):
        return f"Mock Test Attempt by {self.student.username} - Score: {self.score}"






class MockTestSubmission(models.Model):
    total_attended = models.IntegerField(max_length=200)
    unattended = models.CharField()
    test_average_time = models.TimeField()
    score = models.FloatField(default=0)
    completed = models.BooleanField(default=False)
    question_average_time = models.TimeField()
    completion_date = models.TimeField

    def __str__(self):
        return self.total_attended






























