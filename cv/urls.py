from django.urls import path
from . import views

app_name = "cv"

urlpatterns = [
    path("", views.home, name="home"),
    path("cv/<int:pk>/", views.preview, name="preview"),
    path("cv/<int:pk>/download/", views.download_pdf, name="download_pdf"),
]
