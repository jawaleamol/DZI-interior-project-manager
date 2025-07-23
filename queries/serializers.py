from rest_framework import serializers

from .models import Query


class QuerySerializer(serializers.ModelSerializer):
    class Meta:
        model = Query
        fields = [
            'id',
            'project',
            'raised_by',
            'assigned_to',
            'category',
            'title',
            'description',
            'status',
            'priority',
            'created_at',
        ]
