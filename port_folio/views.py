from django.shortcuts import render
from .models import Project, Academic, Skill
from .serializers import ProjectSerializer, ContactSerializer, AcademicSerializer, SkillSerializer
from rest_framework.generics import ListAPIView, RetrieveAPIView, CreateAPIView

class ProjectView(ListAPIView):
    queryset= Project.objects.all()
    serializer_class= ProjectSerializer

class ProjectDetailView(RetrieveAPIView):
    queryset = Project.objects.all()  # Fetch a single Project
    serializer_class = ProjectSerializer  # Use the ProjectSerializer to display the details
    lookup_field = 'id'

class ContactView(CreateAPIView):
    serializer_class= ContactSerializer
    
class AcademicView(ListAPIView):
    queryset= Academic.objects.all()
    serializer_class= AcademicSerializer

class SkillView(ListAPIView):
    queryset= Skill.objects.all()
    serializer_class= SkillSerializer