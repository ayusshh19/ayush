from django.db import models

# Create your models here.
class notesmaking(models.Model):
    username=models.CharField(max_length=20)
    task=models.CharField(max_length=30)
    abouttask=models.CharField(max_length=200)
    
def __str__(self):
    return self.username
