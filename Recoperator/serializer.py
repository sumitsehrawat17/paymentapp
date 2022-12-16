from rest_framework import serializers

from .models import rechargeplans
class Planserializers(serializers.ModelSerializer):
    class Meta:
        model = rechargeplans
        fields = ["op","plan","description"]

