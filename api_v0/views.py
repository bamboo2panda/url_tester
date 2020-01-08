from rest_framework import viewsets
from .serializers import *


class ScanViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Scan.objects.all()

    def get_serializer_class(self):
        if self.action == 'list':
            return ScanPreviewSerializer
        return ScanDetailSerializer
