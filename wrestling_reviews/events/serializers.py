from django.forms import models
from rest_framework import serializers
from .models import Event
from datetime import date

class EventSerializer(serializers.ModelSerializer):
    """
    Serializer بسيط للـ Event مع فاليديشن اختيارية
    """
    class Meta:
        model = Event
        fields = [
            "id",
            "name",
            "date",
            "location",
            "promotion",
            "description",
            "is_ppv",
            "created_at",
            "updated_at",
        ]
        read_only_fields = ["id", "created_at", "updated_at"]

    def validate_name(self, value):
        # مثال: ممنوع اسم فاضي بعد الـ strip
        if not value.strip():
            raise serializers.ValidationError("اسم الحدث لا يجب أن يكون فارغًا.")
        return value

    def validate_date(self, value):
        # مثال: اسمح بالماضي والمستقبل (عادي للأحداث)
        # لو حابب تمنع تاريخ قبل 1900:
        if value.year < 1900:
            raise serializers.ValidationError("تاريخ الحدث غير منطقي (قبل 1900).")
        return value

    def validate_updated_at(self, value):
        # مثال: تأكد أن تاريخ التحديث ليس في المستقبل
        if value > date.today():
            raise serializers.ValidationError("تاريخ التحديث لا يمكن أن يكون في المستقبل.")
        return value
    
class Event(models.Model):
    # الحقول الأخرى
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)