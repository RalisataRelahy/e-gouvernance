from rest_framework import serializers
from .models import Citoyen
from rest_framework import serializers
from .models import Province
from datetime import date
class ProvinceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Province
        fields = ['id', 'nom']


class CitizenSerializer(serializers.ModelSerializer):
    age = serializers.SerializerMethodField()

    class Meta:
        model = Citoyen
        fields = '__all__'

    def get_age(self, obj):
        return obj.age()

    def validate(self, data):
        dob = data.get('date_naissance')
        if dob:
            age = date.today().year - dob.year - (
                (date.today().month, date.today().day) < (dob.month, dob.day)
            )
            if age >= 18 and not data.get('numero_cin'):
                raise serializers.ValidationError({
                    'numero_cin': 'Requis pour les majeurs.'
                })
        return data
