from rest_framework import serializers
from api.models import Report

class ReportSerializer(serializers.ModelSerializer):
    class Meta:
        model = Report
        fields = ("id", "document_id", "description", "created_date", "updated_date", "created_by", "updated_by")
