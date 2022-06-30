from django.urls import path
from .views import ListDateJoinedView, LoginView, UserView

urlpatterns = [
    path("accounts/", UserView.as_view()),
    path("login/", LoginView.as_view()),
    path("accounts/newest/<int:num>/", ListDateJoinedView.as_view())
]