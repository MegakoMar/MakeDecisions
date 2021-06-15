from django.contrib import admin
from django.db import models
from .models import Project, Questions, Answers, Question, QuestionIterTwo, FinalQuestion, FinalAnswer

admin.site.register(Project)
admin.site.register(Questions)
admin.site.register(Answers)
admin.site.register(Question)
admin.site.register(QuestionIterTwo)
admin.site.register(FinalQuestion)
admin.site.register(FinalAnswer)