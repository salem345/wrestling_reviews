from rest_framework import serializers
from .models import Wrestler

class WrestlerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Wrestler
        fields = '__all__'