from rest_framework import serializers
from scan.models import Scan


class ScanPreviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Scan
        fields = [
            'id',
            'title',
            'created_at',
            'announce',
            'url',
        ]


class ScanDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Scan
        fields = [
            'title',
            'created_at',
            'text',
        ]