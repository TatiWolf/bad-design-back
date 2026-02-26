from rest_framework import serializers
from .models import Catalog, DarkPattern,DarkPattern

class DarkPatternSerializer(serializers.ModelSerializer):
    class Meta:
        model = DarkPattern
        fields = "__all__"


class CatalogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Catalog
        fields = "__all__"


class AnotherDarkPatternSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    title = serializers.CharField()


class DarkPatternDetailSerializer(serializers.ModelSerializer):
    previousDarkPattern = serializers.SerializerMethodField()
    nextDarkPattern = serializers.SerializerMethodField()

    class Meta:
        model = DarkPattern
        fields = [
            "id",
            "title",
            "title_another_language_for_list",
            "catalog",
            "descriptions",
            "key_mechanics",
            "key_mechanics_video",
            "consequences_for_the_user",
            "alternatives",
            "previousDarkPattern",
            "nextDarkPattern",
        ]

    # ✅ ОБЯЗАТЕЛЬНО внутри класса
    def get_previousDarkPattern(self, obj):
        previous = (
            DarkPattern.objects
            .filter(catalog=obj.catalog, id__lt=obj.id)
            .order_by("-id")
            .first()
        )

        if not previous:
            previous = (
                DarkPattern.objects
                .filter(catalog=obj.catalog)
                .order_by("-id")
                .first()
            )

        if not previous:
            return None

        return {
            "id": previous.id,
            "title": previous.title
        }

    # ✅ ОБЯЗАТЕЛЬНО внутри класса
    def get_nextDarkPattern(self, obj):
        next_pattern = (
            DarkPattern.objects
            .filter(catalog=obj.catalog, id__gt=obj.id)
            .order_by("id")
            .first()
        )

        if not next_pattern:
            next_pattern = (
                DarkPattern.objects
                .filter(catalog=obj.catalog)
                .order_by("id")
                .first()
            )

        if not next_pattern:
            return None

        return {
            "id": next_pattern.id,
            "title": next_pattern.title
        }    
class DarkPatternListSerializer(serializers.ModelSerializer):
    class Meta:
        model = DarkPattern
        fields = [
            "id",
            "title",
            "title_another_language_for_list",
            "description_for_list",
        ]