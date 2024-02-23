from django.contrib import admin
from .models import Question, Execution, TestCase

admin.site.register(Question)
admin.site.register(Execution)
admin.site.register(TestCase)
