from rest_framework import serializers
from .models import Project, Contact, Academic, Skill

class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model= Project
        fields= '__all__'

class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model= Contact
        fields= '__all__'

class AcademicSerializer(serializers.ModelSerializer):
    class Meta:
        model= Academic
        fields= '__all__'

class SkillSerializer(serializers.ModelSerializer):
    class Meta:
        model= Skill
        fields= '__all__'