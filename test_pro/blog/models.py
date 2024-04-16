from django.db import models
from django.contrib.auth.models import User
import os
from django.urls import reverse


# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=120)
    file = models.FileField(null=True, blank=True, upload_to="Files")
    content = models.TextField()
    date_posted = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f"{self.title} | {self.author.username}"

    def extension(self):
        name, extension = os.path.splitext(self.file.name)
        return extension

    def get_absolute_url(self):
        return reverse("post-detail", kwargs={"pk": self.pk})
