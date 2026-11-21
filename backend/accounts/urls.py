from django.urls import path

from . import views

app_name = "accounts"

urlpatterns = [
    path("signup/", views.signup, name="signup"),
    path("login/", views.MemberLoginView.as_view(), name="login"),
    path("logout/", views.MemberLogoutView.as_view(), name="logout"),
    path("admin-control/", views.admin_control, name="admin_control"),
]
