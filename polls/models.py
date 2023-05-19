from datetime import datetime
from django.db import models
from django.contrib import admin
from django.utils import timezone


class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField(' date published')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


def was_published_recently(self):
    return self.pub_date >= timezone.now() - datetime.timedelta(days=1)


class QuestionList(admin.ModelAdmin):
    search_fields = ("question_text", "pub_date")
    empty_value_display = "-empty-"
    list_display = ("question_text", "pub_date", "created_at")


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class ChoiceAdmin(admin.ModelAdmin):
    search_fields = ("question", "choice_text", "votes")
    empty_value_display = "-empty-"
    list_display = ("question", "choice_text", "votes", "created_at")
