from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CitizenViewSet

router = DefaultRouter()
router.register(r'citoyen', CitizenViewSet, basename='citoyen')

urlpatterns = [
    path('api/', include(router.urls)),  # ← maintenant /api/citoyen/ existe
]
