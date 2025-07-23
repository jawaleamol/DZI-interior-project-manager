from rest_framework import serializers

from .models import Document


class DocumentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Document
        fields = [
            'id',
            'project',
            'uploaded_by',
            'category',
            'title',
            'file',
            'version',
            'is_active',
        ]
