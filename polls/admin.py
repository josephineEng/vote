from django.contrib import admin

from .models import Question, Choice

admin.site.site_header = "SITE ADMIN"
admin.site.site_title = "CONFIGURATION AREA"
admin.site.index_title = "MAKE SITE CHANGES HERE"


class ChoiceInline(admin.TabularInline):
  model = Choice
  extra = 3


class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [(None, {'fields': ['question_text']}),
                 ('Date Information', {'fields': ['pub_date'], 'classes': ['collapse']}), ]
    inlines = [ChoiceInline]


# admin.site.register(Question)
# admin.site.register(Choice)
admin.site.register(Question,QuestionAdmin)