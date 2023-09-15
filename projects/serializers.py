from rest_framework import serializers
from .models import Project


class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = (
            'id', 'projectStatus', 'projectTitle', 'projectPlace', 'estimatedImplementationDate', 'slogan', "about",
            "goal", "support", "shortDesc", "longDesc", "projectImage", "createdBy", "createdByName", "createdDate",
            "projectValue",
            "totalShares", "shareValue", "maxSharesPerPerson", "sharesTaken", "adminAdvice")
