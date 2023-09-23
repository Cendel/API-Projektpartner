from django.db import models
from projects.models import Project
import os


class FileExtensionGetter:
    def __call__(self, instance, filename):
        return os.path.splitext(filename)[1]


class Attachment(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='attachments')
    file = models.FileField(upload_to='project_attachments_files/', null=True, blank=True)
    file_type = models.CharField(max_length=100, null=True, blank=True)
    file_extension = models.CharField(max_length=20, null=True, blank=True)

    def save(self, *args, **kwargs):
        if self.file:
            self.file_type = self.file.content_type
            self.file_extension = os.path.splitext(self.file.name)[1]
        super().save(*args, **kwargs)
