from rest_framework import viewsets
from rest_framework import permissions
from rest_framework import filters
from api.serializers import ReportSerializer
from api.models import Report

class ReportView(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Report.objects.all()
    serializer_class = ReportSerializer
    permission_classes = [permissions.AllowAny]
    filter_backends = [filters.SearchFilter]
    search_fields = ['id', 'document_id']