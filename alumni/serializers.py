from rest_framework import serializers
from .models import alumnus

class alumnusSerializer(serializers.ModelSerializer):
    class Meta:
        model = alumnus
        fields = '__all___'
        