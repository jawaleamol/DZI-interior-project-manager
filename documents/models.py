from django.conf import settings
from django.db import models

from projects.models import Project

User = settings.AUTH_USER_MODEL


class Document(models.Model):
    CATEGORY_CHOICES = [
        ('boq', 'BOQ (Bill of Quantity)'),
        ('designs', 'Designs & Layouts'),
        ('permits', 'Permits & Approvals'),
        ('material_specs', 'Material Specifications'),
        ('progress_reports', 'Progress Reports'),
    ]
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    uploaded_by = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)
    title = models.CharField(max_length=200)
    file = models.FileField(upload_to='documents/')
    version = models.PositiveIntegerField(default=1)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.title
