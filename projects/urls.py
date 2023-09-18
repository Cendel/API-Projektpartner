from django.urls import path
from .views import ProjectCreateAPIView, ProjectDetailView, ProjectsListByStatusView, ProjectsListByAdminAdviceView, \
    ProjectDetailAuthView, ProjectFollowerUpdateView

urlpatterns = [
    # Diğer URL şablonları burada
    path('create/', ProjectCreateAPIView.as_view(), name='project-create'),
    path('list/status/', ProjectsListByStatusView.as_view(), name='list-by-status'),
    path('list/advice/', ProjectsListByAdminAdviceView.as_view(), name='list-by-advice'),
    path('<int:pk>/', ProjectDetailView.as_view(), name='project-detail'),
    path('auth/<int:pk>/', ProjectDetailAuthView.as_view(), name='project-auth-detail'),
    path('follow/<int:pk>/', ProjectFollowerUpdateView.as_view(), name='project-participant-join'),
]
