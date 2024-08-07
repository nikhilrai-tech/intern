from django.db import models

# Create your models here.
class techstack(models.Model):
    class_id=models.IntegerField(primary_key=True,auto_created=True)
    name=models.CharField(max_length=20)
    created_at=models.DateField(auto_now_add=True)
    refrence=models.CharField(max_length=2)
