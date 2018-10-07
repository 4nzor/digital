from rest_framework import serializers
from second.models import Organization


class SnippetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Organization
        fields = ('__all__')