# gestionpop/urls.py (Votre fichier principal)

from django.contrib import admin
from django.urls import path, include

# 1. Importez les vues JWT
from rest_framework_simplejwt.views import (
    TokenObtainPairView,  # Pour obtenir les tokens (le login)
    TokenRefreshView,    # Pour rafraîchir le token d'accès
)


urlpatterns = [
    path('admin/', admin.site.urls),
    
    # 2. Ajoutez les URLs de l'API d'authentification
    # Le POST sur ce chemin prendra username et password, et renverra access et refresh tokens
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    # Le POST sur ce chemin prendra le refresh token et renverra un nouveau access token
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    
    # Vos URLs d'application (comme /api/provinces/ via population.urls)
    path('', include('population.urls')),
]