# population/urls.py (Version simplifiée et alignée avec JWT)

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CitizenViewSet, RegisterView
from .views import ProvinceViewSet
# Note: On retire l'import et l'utilisation de LoginView si on utilise le login JWT du fichier principal

router = DefaultRouter()
router.register(r'citoyen', CitizenViewSet, basename='citoyen')
router.register(r'provinces', ProvinceViewSet, basename='province')

urlpatterns = [
    # Tous les chemins d'API pour Citoyen et Province sont sous /api/
    path('api/', include(router.urls)), 
    path('api/register/', RegisterView.as_view(), name='register'),
]

# Les URLs d'API disponibles sont :
# - http://127.0.0.1:8000/api/citoyen/
# - http://127.0.0.1:8000/api/provinces/
#
# L'URL de LOGIN (JWT) est dans le fichier principal :
# - http://127.0.0.1:8000/api/token/