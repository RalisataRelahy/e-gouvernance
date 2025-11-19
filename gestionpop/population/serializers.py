from rest_framework import serializers
from .models import Citoyen
from rest_framework import serializers
from .models import Province
from datetime import date
from django.contrib.auth.models import User # 👈 Importez le modèle User
from django.db import IntegrityError # Pour gérer les doublons

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

    def validate(self, data): # pyright: ignore[reportIncompatibleMethodOverride]
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

class UserSerializer(serializers.ModelSerializer):
    # Ce champ sera utilisé pour valider que le mot de passe est tapé deux fois correctement
    password2 = serializers.CharField(style={'input_type': 'password'}, write_only=True)

    class Meta:
        model = User
        # Nous avons besoin de ces champs pour l'inscription
        fields = ['username', 'email', 'password', 'password2']
        extra_kwargs = {
            'password': {'write_only': True} # S'assurer que le mot de passe n'est jamais retourné en lecture
        }

    def validate(self, data): # pyright: ignore[reportIncompatibleMethodOverride]
        """Vérifie que les deux mots de passe correspondent et que l'utilisateur n'existe pas déjà (bien que la DB le gère aussi)."""
        
        # 1. Validation de l'égalité des mots de passe
        password = data.get('password')
        password2 = data.get('password2')
        
        if password != password2:
            raise serializers.ValidationError({"password": "Les deux mots de passe doivent être identiques."})
            
        # 2. Validation de l'unicité (l'unicité est déjà gérée par la DB mais une vérif explicite est plus propre)
        if User.objects.filter(username=data.get('username')).exists():
             raise serializers.ValidationError({"username": "Ce nom d'utilisateur est déjà pris."})
        
        # Le champ password2 ne doit pas être transmis à la méthode create()
        data.pop('password2') 
        return data

    def create(self, validated_data):
        """Crée l'utilisateur et hache le mot de passe."""
        try:
            # Utilisez create_user pour hacher correctement le mot de passe
            user = User.objects.create_user(
                username=validated_data['username'],
                email=validated_data['email'],
                password=validated_data['password']
            )
            # S'assurer qu'ils sont actifs (c'est le comportement par défaut de create_user, mais bonne pratique)
            # user.is_active = True
            user.save()
            return user
        except IntegrityError:
            # Gérer les erreurs d'unicité (par ex. email déjà utilisé si vous le rendez unique)
            raise serializers.ValidationError({"detail": "Erreur lors de la création de l'utilisateur."})