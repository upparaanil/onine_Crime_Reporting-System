from django.contrib import admin
from . models import User,Feedback


admin.site.register(User)
# admin.site.register(Feedback)

# Register your models here.
class FeedbackAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'date', 'message',)
    list_filter = ('name', 'date',)
  

admin.site.register(Feedback, FeedbackAdmin)