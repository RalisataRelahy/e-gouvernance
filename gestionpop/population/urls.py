from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CitizenViewSet
from .views import ProvinceViewSet

router = DefaultRouter()
router.register(r'citoyen', CitizenViewSet, basename='citoyen')
router.register(r'provinces', ProvinceViewSet, basename='province')

urlpatterns = [
    path('api/', include(router.urls)),  # ← maintenant /api/citoyen/ existe
]
