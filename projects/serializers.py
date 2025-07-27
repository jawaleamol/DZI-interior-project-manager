from rest_framework import serializers

from .models import Project, ProjectMembership, ProjectTimeline


class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = [
            'id',
            'name',
            'description',
            'customer',
            'created_at',
        ]


class ProjectMembershipSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProjectMembership
        fields = ['id', 'project', 'user', 'role']


class ProjectTimelineSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProjectTimeline
        fields = ['id', 'project', 'name', 'start_date', 'end_date']
