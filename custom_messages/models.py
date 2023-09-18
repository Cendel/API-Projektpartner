from django.db import models
from users.models import User


class Message(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    text = models.TextField()

    def __str__(self):
        return f"Message from {self.user.name}, Title: {self.title}"
