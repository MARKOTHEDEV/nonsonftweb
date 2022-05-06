from django.contrib import admin
from . import models
# Register your models here.


admin.site.register(models.ContactUs)
admin.site.register(models.CvData)



# class AnswerInline(admin.TabularInline):
#     model = models.Quetions

# class QuestionAdmin(admin.ModelAdmin):
#     inlines = [AnswerInline]

# admin.site.register(models.Question, QuestionAdmin)
# admin.site.register(models.Answer)

class YourModelAdmin(admin.ModelAdmin):
    list_filter =['email']
    list_display =("email",'quetion','anser')
admin.site.register(models.Survey,YourModelAdmin)
admin.site.register(models.Quetions)

admin.site.register(models.closeSurvey)