from django.urls import path
from . import views

urlpatterns = [
    path("job", views.JobListCreateView.as_view(), name="job-list"),
    path("job/<int:pk>",views.JobDetailView.as_view(),name="job-detail"),
]
