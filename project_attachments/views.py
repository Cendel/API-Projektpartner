from core.permissions import IsProjectOwner
from .serializers import AttachmentSerializer
from rest_framework.generics import CreateAPIView, ListAPIView, DestroyAPIView
from .models import Attachment
from projects.models import Project
from rest_framework.permissions import IsAuthenticated


class AttachmentCreateAPIView(CreateAPIView):
    serializer_class = AttachmentSerializer
    permission_classes = IsProjectOwner


class AttachmentsByProjectIdListAPIView(ListAPIView):
    serializer_class = AttachmentSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        project_to_be_fetched = self.request.query_params.get('projectId')
        queryset = Attachment.objects.filter(project_id=project_to_be_fetched)
        return queryset


class AttachmentDestroyAPIView(DestroyAPIView):
    queryset = Attachment
    serializer_class = AttachmentSerializer
    permission_classes = IsProjectOwner
