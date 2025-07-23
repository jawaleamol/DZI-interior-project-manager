from django.conf import settings
from django.db import models

from projects.models import Project

User = settings.AUTH_USER_MODEL


class Query(models.Model):
    STATUS_CHOICES = [
        ('new', 'New'),
        ('assigned', 'Assigned'),
        ('ready_for_review', 'Ready for Review'),
        ('pending', 'Pending'),
        ('in_progress', 'In Progress'),
        ('solved', 'Solved'),
    ]
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    raised_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='raised_queries')
    assigned_to = models.ForeignKey(User, on_delete=models.CASCADE, related_name='assigned_queries', null=True, blank=True)
    category = models.CharField(max_length=50)
    title = models.CharField(max_length=200)
    description = models.TextField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='new')
    priority = models.CharField(max_length=10)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
