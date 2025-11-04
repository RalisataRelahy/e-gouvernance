from rest_framework import viewsets, filters
from django_filters.rest_framework import DjangoFilterBackend
from .models import Citoyen
from .serializers import CitizenSerializer
from rest_framework import viewsets
from .models import Province
from .serializers import ProvinceSerializer

class ProvinceViewSet(viewsets.ModelViewSet):
    queryset = Province.objects.all()
    serializer_class = ProvinceSerializer

class CitizenViewSet(viewsets.ModelViewSet):
    queryset = Citoyen.objects.all()
    serializer_class = CitizenSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ['province']  # 🔥 Pour filtrer par province
    search_fields = ['nom', 'prenoms', 'numero_cin', 'province', 'quartier']  # 🔍 Recherche full-text
