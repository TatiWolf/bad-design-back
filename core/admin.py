from django.contrib import admin
from .models import Catalog, DarkPattern, Study


class DarkPatternInline(admin.TabularInline):
    model = DarkPattern
    extra = 1


@admin.register(Catalog)
class CatalogAdmin(admin.ModelAdmin):
    inlines = [DarkPatternInline]
    readonly_fields = ("title", "title_another_language", "slug")
    
@admin.register(Study)
class StudyAdmin(admin.ModelAdmin):
    list_display = ("id", "author_of_the_article", "created_year", "title","original_title","url","description")
    
