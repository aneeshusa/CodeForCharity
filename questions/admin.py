from django.contrib import admin
from questions.models import Topic, Question, Test

class QuestionInline(admin.StackedInline):
    model = Question
    extra = 4

class TopicAdmin(admin.ModelAdmin):
    inlines = [QuestionInline]

admin.site.register(Topic, TopicAdmin)
admin.site.register(Test)
