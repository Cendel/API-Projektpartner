from rest_framework import serializers
from rest_framework.permissions import IsAuthenticated

from .models import Project


class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = (
            'id', 'projectStatus', 'projectTitle', 'projectPlace', 'estimatedImplementationDate', 'slogan', "about",
            "goal", "support", "shortDesc", "longDesc", "projectImage", "createdBy", "createdByName", "createdDate",
            "projectValue", "totalShares", "shareValue", "maxSharesPerPerson", "sharesTaken", "adminAdvice",
            "followerList")


class ProjectFollowerUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ['followerList']

# class ProjectSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Project
#         fields = (
#             'id', 'projectStatus', 'projectTitle', 'projectPlace', 'slogan', "about",
#             "goal", "support", "shortDesc", "longDesc", "createdBy", "createdByName", "createdDate",
#             "projectValue",
#             "totalShares", "shareValue", "maxSharesPerPerson", "sharesTaken", "adminAdvice")
