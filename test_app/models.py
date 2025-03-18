from django.db import models
from student.models import Organization
from django.conf import settings
from datetime import timedelta
from django.contrib.auth.models import User


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
    organization =models.ForeignKey(Organization, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return str(self.question_no)




class MockTest(models.Model):
    student = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="mock_tests")
    completed = models.BooleanField(default=False)
    organization = models.ForeignKey(Organization, on_delete=models.SET_NULL, null=True, blank=True)


    def __str__(self):
        return f"Mock Test Attempt by {self.student.username}"



class MockTestSubmission(models.Model):

    mock_test = models.ForeignKey(MockTest, on_delete=models.CASCADE)
    student = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True, blank=True)
    question = models.ForeignKey(Question, on_delete=models.CASCADE, null=True, blank=True)
    total_attended = models.IntegerField(null=True)
    unattended = models.IntegerField(default=0)
    test_average_time = models.DurationField(null=True, blank=True)
    question_average_time = models.DurationField(default=timedelta(seconds=60))
    score = models.FloatField(default=0)
    completed = models.BooleanField(default=False)
    is_correct = models.BooleanField(default=False)
    submitted_at = models.DateTimeField(null=True, blank=True, auto_now_add=True)
    selected_option = models.CharField(
        max_length=1,
        choices=[('A', 'Option A'), ('B', 'Option B'), ('C', 'Option C'), ('D', 'Option D')],
        null=True, blank=True
    )


    def __str__(self):
        return str(self.mock_test)




class PracticalTest(models.Model):

    student = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True, blank=True)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    organization = models.ForeignKey(Organization, on_delete=models.SET_NULL, null=True, blank=True)
    completed = models.BooleanField(default=False)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)


    def __str__(self):
        return f" Practical Test Attempt by {self.student.username}"


class PracticalTestSubmission(models.Model):
    practical_test = models.ForeignKey(PracticalTest, on_delete=models.CASCADE)
    student = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True, blank=True)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    answers = models.CharField()
    score = models.FloatField(null=True, blank=True)
    unattended = models.IntegerField(default=0)
    total_attended = models.IntegerField(null=True)
    test_average_time = models.DurationField(null=True, blank=True)
    completed = models.BooleanField(default=False)
    submitted_at = models.DateTimeField(null=True, blank=True, auto_now_add=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.practical_test
























