from django.contrib import admin

from .models import Question, QuestionList
from polls.models import Choice, ChoiceAdmin

admin.site.register(Question, QuestionList)
admin.site.register(Choice, ChoiceAdmin)
# no need here
