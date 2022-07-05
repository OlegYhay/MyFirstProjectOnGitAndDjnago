from django.contrib import admin

# Register your models here.
from questions.models import Questions, Test, Answer

admin.site.register(Questions)
admin.site.register(Test)
admin.site.register(Answer)