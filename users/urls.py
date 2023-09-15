from django.urls import path
from .views import RegisterView, LoginView, UpdateUserView, UserListForAdminView, UserDetailView

urlpatterns = [
    path('register/', RegisterView.as_view(), name="register"),
    path('login/', LoginView.as_view(), name="login"),
    path('user/', UpdateUserView.as_view(), name="login"),
    path('auth/users/', UserListForAdminView.as_view(), name="user_page_all"),
    path('user/<int:pk>/', UserDetailView.as_view(), name='user-detail'),
    path('user/<int:pk>/update/', UserDetailView.as_view(), name='user-update'),
    path('user/<int:pk>/delete/', UserDetailView.as_view(), name='user-delete'),

]
