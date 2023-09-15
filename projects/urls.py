from django.urls import path
from .views import ProjectCreateAPIView, ProjectDetailView, ProjectsListByStatusView, ProjectsListByAdminAdviceView

urlpatterns = [
    # Diğer URL şablonları burada
    path('create/', ProjectCreateAPIView.as_view(), name='project-create'),
    path('list/status/', ProjectsListByStatusView.as_view(), name='project-list'),
    path('list/advice/', ProjectsListByAdminAdviceView.as_view(), name='project-list'),
    path('<int:pk>/', ProjectDetailView.as_view(), name='project-retrieve'),
]
