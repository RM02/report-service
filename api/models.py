from django.db import models
from uuid import uuid4

# Create your models here.
class Report(models.Model):

    id = models.CharField(primary_key=True, default=uuid4(), max_length=250, auto_created=True)

    document_id = models.CharField(max_length=250)

    description = models.CharField(max_length=250)

    created_date=models.DateTimeField(auto_now_add=True)
    updated_date=models.DateTimeField(auto_now_add=True)

    created_by = models.CharField(max_length=250, default='admin', auto_created=True)
    updated_by = models.CharField(max_length=250, default='admin', auto_created=True)

