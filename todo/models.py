from django.db import models
from django.contrib.auth.models import User

class userprofile(models.Model):
     user=models.OneToOneField(User, on_delete=models.CASCADE)
     bio=models.TextField(blank=True)
     location=models.CharField(max_length=30, blank=True)
     birth_date=models.DateField(null=True, blank=True)

     def __str__(self):
         return self.user.username
class Task(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    title=models.CharField(max_length=100)
    description=models.TextField(blank=True)
    due_date=models.DateField()
    is_deleted=models.BooleanField(default=False)
    category=models.CharField(max_length=50)
    
    def __str__(self):
        return self.title