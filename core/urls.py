from rest_framework.routers import DefaultRouter
from django.urls import path, include
from .views import CatalogViewSet, DarkPatternViewSet

router = DefaultRouter()
router.register(r"catalogs", CatalogViewSet)
router.register(r"dark-patterns", DarkPatternViewSet)

urlpatterns = [
    path("", include(router.urls)),
]