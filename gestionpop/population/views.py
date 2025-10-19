from rest_framework import viewsets, filters
from .models import Citoyen
from .serializers import CitizenSerializer

class CitizenViewSet(viewsets.ModelViewSet):
    queryset = Citoyen.objects.all()
    serializer_class = CitizenSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['nom', 'prenoms', 'numero_cin', 'province', 'quartier']
