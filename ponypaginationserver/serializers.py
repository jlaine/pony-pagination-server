from rest_framework import serializers

from .models import Pony


class PonySerializer(serializers.ModelSerializer):
    class Meta:
        model = Pony
        fields = (
            "id",
            "is_available",
            "name",
        )
