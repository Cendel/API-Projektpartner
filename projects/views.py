from rest_framework.generics import CreateAPIView, RetrieveAPIView, ListAPIView, RetrieveUpdateDestroyAPIView, \
    UpdateAPIView
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.response import Response
from rest_framework import status
from .models import Project
from .serializers import ProjectSerializer, ProjectFollowerUpdateSerializer, ProjectListForTablesSerializer
from rest_framework.permissions import IsAuthenticated, IsAdminUser


class ProjectCreateAPIView(CreateAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    parser_classes = (MultiPartParser, FormParser)
    permission_classes = [IsAuthenticated]

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        project = serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class ProjectsListByStatusView(ListAPIView):
    serializer_class = ProjectSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        status_param = True if self.request.query_params.get('projectStatus') == "true" else False
        queryset = Project.objects.filter(projectStatus=status_param)
        return queryset


class ProjectsListByAdminAdviceView(ListAPIView):
    serializer_class = ProjectSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        status_param = True if self.request.query_params.get('adminAdvice') == "true" else False
        queryset = Project.objects.filter(adminAdvice=status_param)
        return queryset


class ProjectDetailView(RetrieveAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    permission_classes = [IsAuthenticated]


class ProjectDetailAuthView(RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAdminUser]
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer


class ProjectFollowerUpdateView(UpdateAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectFollowerUpdateSerializer
    permission_classes = [IsAuthenticated]

    def perform_update(self, serializer):
        user = self.request.user
        project = self.get_object()
        project.participantList.add(user)
        serializer.save(followerList=project.participantList.all())

# class IsProjectOwnerOrAdmin(BasePermission):
#     """
#     Custom permission to allow only project owner or admin to update or delete.
#     """
#
#     def has_object_permission(self, request, view, obj):
#         # Check if the user is an admin or the project creator
#         return obj.createdBy == request.user or request.user.is_staff
#
# class ProjectDetailView(RetrieveUpdateDestroyAPIView):
#     queryset = Project.objects.all()
#     serializer_class = ProjectSerializer
#     permission_classes = [IsProjectOwnerOrAdmin]
