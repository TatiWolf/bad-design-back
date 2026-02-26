from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import Catalog, DarkPattern
from .serializers import (
    CatalogSerializer,
    DarkPatternSerializer,
    DarkPatternDetailSerializer,
    DarkPatternListSerializer
)


class CatalogViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Catalog.objects.all()
    serializer_class = CatalogSerializer

    # список паттернов каталога (+ фильтрация по section)
    @action(detail=True, methods=["get"], url_path="dark-patterns")
    def dark_patterns(self, request, pk=None):
        catalog = self.get_object()

        patterns = catalog.dark_patterns.all().order_by("order")

        serializer = DarkPatternListSerializer(patterns, many=True)
        return Response(serializer.data)


    # детальная информация о конкретном паттерне
    @action(
        detail=True,
        methods=["get"],
        url_path=r"dark-patterns/(?P<pattern_id>[^/.]+)"
    )
    def dark_pattern_detail(self, request, pk=None, pattern_id=None):
        pattern = DarkPattern.objects.get(
            pk=pattern_id,
            catalog_id=pk
        )
        serializer = DarkPatternDetailSerializer(pattern)
        return Response(serializer.data)


class DarkPatternViewSet(viewsets.ModelViewSet):
    queryset = DarkPattern.objects.all()
    serializer_class = DarkPatternSerializer
    
    
