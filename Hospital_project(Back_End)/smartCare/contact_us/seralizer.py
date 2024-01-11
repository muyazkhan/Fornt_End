from rest_framework import serializers
from .models import contactModels


class contact_us(serializers.ModelSerializer):
    class Meta:
        model = contactModels
        fields = '__all__'