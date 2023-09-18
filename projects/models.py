from django.db import models
from users.models import User


class Project(models.Model):
    projectStatus = models.BooleanField(default=False)
    projectTitle = models.CharField(max_length=255)
    projectPlace = models.CharField(max_length=255)
    estimatedImplementationDate = models.DateTimeField(blank=True, null=True)
    slogan = models.CharField(max_length=50)
    about = models.TextField()
    goal = models.TextField()
    support = models.TextField()
    shortDesc = models.CharField(max_length=200)
    longDesc = models.TextField()
    projectImage = models.ImageField(upload_to='project_images/')
    createdBy = models.ForeignKey(User, related_name="projects", on_delete=models.CASCADE)
    createdByName = models.CharField(max_length=255, blank=True)
    createdDate = models.DateTimeField(auto_now_add=True)
    followerList = models.ManyToManyField(User, related_name='followed_projects', blank=True)
    participantList = models.ManyToManyField(User, related_name='participated_projects', blank=True)
    participantCount = models.IntegerField(default=0)
    projectValue = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    totalShares = models.IntegerField(default=0)
    shareValue = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    maxSharesPerPerson = models.IntegerField(default=0)
    sharesTaken = models.IntegerField(default=0)
    adminAdvice = models.BooleanField(default=False)

    def save(self, *args, **kwargs):
        if self.createdBy:
            self.createdByName = self.createdBy.name  # Kullanıcı adını al
        super().save(*args, **kwargs)

    #     self.participantCount = self.participantList.count()
    #     super(Project, self).save(*args, **kwargs)

# class Attachment(models.Model):
#     project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='attachments')
#     file = models.FileField(upload_to='project_attachments/', null=True, blank=True)
