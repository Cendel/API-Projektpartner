from rest_framework import serializers
from .models import ShareOwnership
from projects.models import Project
from users.models import User


class ShareOwnershipSerializer(serializers.ModelSerializer):
    class Meta:
        Model = Project
        Fields = "__all__"
