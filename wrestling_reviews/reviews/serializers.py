from rest_framework import serializers
from .models import Review
from wrestlers.models import Wrestler


class ReviewSerializer(serializers.ModelSerializer):
    wrestlers = serializers.PrimaryKeyRelatedField(
        many=True,
        queryset=Wrestler.objects.all()
    )

    def to_internal_value(self, data):
        data = data.copy()
        wrestlers = data.get("wrestlers")

        if isinstance(wrestlers, str):  
            try:
            
                parts = [x.strip() for x in wrestlers.replace("and", ",").split(",") if x.strip()]
                data["wrestlers"] = [int(x) for x in parts]
            except ValueError:
                raise serializers.ValidationError({"wrestlers": "IDs must be numbers separated by commas or 'and'"})

        return super().to_internal_value(data)

    class Meta:
        model = Review
        fields = '__all__'