from django.db import models
from users.models import User
from projects.models import Project


class ShareOwnership(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    shares = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f"{self.user.name} owns {self.shares} shares in {self.project}"
