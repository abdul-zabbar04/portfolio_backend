from django.urls import path
from .views import ProjectView, ProjectDetailView, ContactView, AcademicView, SkillView

urlpatterns = [
    path('projects/', ProjectView.as_view(), name='project-list'),
    path('project/<int:id>/', ProjectDetailView.as_view(), name='project-details'),
    path('contact/', ContactView.as_view(), name='contact'),
    path('academic/', AcademicView.as_view(), name='academic'),
    path('skills/', SkillView.as_view(), name='skills'),
]