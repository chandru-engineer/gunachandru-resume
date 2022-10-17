from unittest.util import _MAX_LENGTH
from django.db import models

# Create your models here.
class Projects(models.Model):
    title = models.CharField(max_length = 200)
    git_link = models.CharField(max_length = 200)
    small_des = models.CharField(max_length=200)
    project_image = models.ImageField(upload_to='images/')
    added = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.title
    
    class Meta:
        ordering = ['-added']