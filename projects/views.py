from rest_framework import viewsets

from .models import Project, ProjectMembership, ProjectTimeline
from .serializers import (
    ProjectSerializer,
    ProjectMembershipSerializer,
    ProjectTimelineSerializer,
)


class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer


class ProjectMembershipViewSet(viewsets.ModelViewSet):
    queryset = ProjectMembership.objects.all()
    serializer_class = ProjectMembershipSerializer


class ProjectTimelineViewSet(viewsets.ModelViewSet):
    queryset = ProjectTimeline.objects.all()
    serializer_class = ProjectTimelineSerializer

from django.shortcuts import render

# Create your views here.
