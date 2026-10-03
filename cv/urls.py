from django.urls import path

from . import views


app_name = "cv"


urlpatterns = [
    # Main CareerForge pages
    path("", views.home, name="home"),
    path("cv/<int:pk>/", views.preview, name="preview"),
    path(
        "cv/<int:pk>/download/",
        views.download_pdf,
        name="download_pdf"
    ),

    # Authentication
    path("register/", views.register, name="register"),
    path("login/", views.login_view, name="login"),
    path("logout/", views.logout_view, name="logout"),
]