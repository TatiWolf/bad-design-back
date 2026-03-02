from rest_framework.routers import DefaultRouter
from django.urls import path, include
from .views import CatalogViewSet, DarkPatternViewSet, StudyViewSet

router = DefaultRouter()
router.register(r"catalogs", CatalogViewSet)
router.register(r"dark-patterns", DarkPatternViewSet)
router.register(r"studies", StudyViewSet)


urlpatterns = [
    path("", include(router.urls)),
]