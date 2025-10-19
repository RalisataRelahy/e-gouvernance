from rest_framework import serializers
from .models import Citoyen

class CitizenSerializer(serializers.ModelSerializer):
    class Meta:
        model = Citoyen
        fields = '__all__'
