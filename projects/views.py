from rest_framework.generics import CreateAPIView, RetrieveAPIView, ListAPIView
from .models import Project
from .serializers import ProjectSerializer


class ProjectCreateAPIView(CreateAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer


class ProjectsListByStatusView(ListAPIView):
    serializer_class = ProjectSerializer

    def get_queryset(self):
        status_param = True if self.request.query_params.get('projectStatus') == "true" else False
        queryset = Project.objects.filter(projectStatus=status_param)
        return queryset


class ProjectsListByAdminAdviceView(ListAPIView):
    serializer_class = ProjectSerializer

    def get_queryset(self):
        status_param = True if self.request.query_params.get('adminAdvice') == "true" else False
        queryset = Project.objects.filter(adminAdvice=status_param)
        return queryset


class ProjectDetailView(RetrieveAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
