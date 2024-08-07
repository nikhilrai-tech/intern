from django.contrib import admin
from . models import *

@admin.register(techstack)
class techstackadmin(admin.ModelAdmin):
    list_display=["class_id","name","created_at"]