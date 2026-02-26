from django.contrib import admin
from .models import Catalog, DarkPattern


class DarkPatternInline(admin.TabularInline):
    model = DarkPattern
    extra = 1


@admin.register(Catalog)
class CatalogAdmin(admin.ModelAdmin):
    inlines = [DarkPatternInline]
    readonly_fields = ("title", "title_another_language", "slug")