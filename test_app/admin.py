from django.contrib import admin
from .models import Subject, Chapter, Question, MockTest, MockTestSubmission, PracticalTest, PracticalTestSubmission

admin.site.register(Subject)
admin.site.register(Chapter)
admin.site.register(Question)
admin.site.register(MockTest)
admin.site.register(MockTestSubmission)
admin.site.register(PracticalTest)
admin.site.register(PracticalTestSubmission)