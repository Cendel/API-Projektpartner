from django.urls import path
from .views import ProjectCreateAPIView, ProjectDetailView, ProjectsListByStatusView, ProjectsListByAdminAdviceView, \
    ProjectDetailAuthView, ProjectFollowerUpdateView, ProjectListForUserTablesView

urlpatterns = [
    # Diğer URL şablonları burada
    path('create/', ProjectCreateAPIView.as_view(), name='project-create'),
    path('list/status/', ProjectsListByStatusView.as_view(), name='list_by_status'),
    path('list/advice/', ProjectsListByAdminAdviceView.as_view(), name='list_by_advice'),
    path('listforusertables/', ProjectListForUserTablesView.as_view(), name='list_for_user_tables'),
    path('<int:pk>/', ProjectDetailView.as_view(), name='project_detail'),
    path('auth/<int:pk>/', ProjectDetailAuthView.as_view(), name='project_auth_detail'),
    path('follow/<int:pk>/', ProjectFollowerUpdateView.as_view(), name='project_participant_join'),
]
