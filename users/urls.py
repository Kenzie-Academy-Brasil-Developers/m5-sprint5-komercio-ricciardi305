from django.urls import path
from .views import ListDateJoinedView, LoginView, UserView, UpdateUserView, IsActiveAdminView

urlpatterns = [
    path("accounts/", UserView.as_view()),
    path("login/", LoginView.as_view()),
    path("accounts/newest/<int:num>/", ListDateJoinedView.as_view()),
    path('accounts/<pk>/', UpdateUserView.as_view()),
    path("accounts/<pk>/management/", IsActiveAdminView.as_view())
]