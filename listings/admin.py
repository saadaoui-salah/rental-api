from django.contrib import admin
from .models import *

admin.site.register(PropertyType)
admin.site.register(Property)
admin.site.register(Image)
admin.site.register(DetailsSection)
admin.site.register(StepSection)
admin.site.register(Question)
admin.site.register(Answer)
admin.site.register(QuestionChoice)
admin.site.register(AnswerChoice)