from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User

class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    image = models.FileField(upload_to='posts/files/', blank=True, null=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE) #will need to change user to whatever auth is called
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

