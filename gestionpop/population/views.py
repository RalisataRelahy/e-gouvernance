from rest_framework import viewsets, filters
from django_filters.rest_framework import DjangoFilterBackend
from .models import Citoyen
from .serializers import CitizenSerializer
from rest_framework import viewsets
from .models import Province
from .serializers import ProvinceSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken

class ProvinceViewSet(viewsets.ModelViewSet):
    queryset = Province.objects.all()
    serializer_class = ProvinceSerializer

class CitizenViewSet(viewsets.ModelViewSet):
    queryset = Citoyen.objects.all()
    serializer_class = CitizenSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ['province']  # 🔥 Pour filtrer par province
    search_fields = ['nom', 'prenoms', 'numero_cin', 'province', 'quartier']  # 🔍 Recherche full-text


class LoginView(APIView):
    def post(self, request):
        username = request.data.get('login')
        password = request.data.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            refresh = RefreshToken.for_user(user)
            return Response({
                'token': str(refresh.access_token),
                'refresh': str(refresh)
            })
        return Response({'error': 'Identifiants invalides'}, status=status.HTTP_401_UNAUTHORIZED)

# population/views.py (Ajoutez cette nouvelle vue)

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import UserSerializer # Importer le serializer créé ci-dessus

class RegisterView(APIView):
    # Désactiver l'authentification pour cette vue (on ne peut pas s'inscrire si on est connecté)
    permission_classes = [] 
    authentication_classes = [] 

    def post(self, request):
        serializer = UserSerializer(data=request.data)
        
        if serializer.is_valid():
            user = serializer.save()
            # En option: Générer directement les tokens JWT après inscription
            # Si vous voulez l'utilisateur se connecte automatiquement après l'inscription,
            # vous pouvez ajouter ici la logique pour générer et renvoyer les tokens.
            
            return Response(
                {"message": "Inscription réussie. Vous pouvez maintenant vous connecter.", 
                 "username": user.username},  # pyright: ignore[reportAttributeAccessIssue]
                status=status.HTTP_201_CREATED
            )
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)