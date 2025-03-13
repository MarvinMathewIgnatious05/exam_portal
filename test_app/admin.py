from django.contrib import admin
from .models import Subject, Chapter, Question, MockTest

admin.site.register(Subject)
admin.site.register(Chapter)
admin.site.register(Question)
admin.site.register(MockTest)
