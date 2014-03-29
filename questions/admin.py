from django.contrib import admin
from questions.models import Topic, Question, Test

class QuestionInline(admin.StackedInline):
    model = Question
    extra = 4

class TopicAdmin(admin.ModelAdmin):
    inlines = [QuestionInline]

admin.site.register(Topic, TopicAdmin)
admin.site.register(Test)

#adding admin features for the user extension 
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User

from questions.models import UserExtension

class ExtensionInline(admin.StackedInline):
    model = UserExtension
    can_delete = False
    verbose_name_plural = 'User'

# Define a new User admin
class UserAdmin(UserAdmin):
    inlines = (ExtensionInline, )

# Re-register UserAdmin
admin.site.unregister(User)
admin.site.register(User, UserAdmin)