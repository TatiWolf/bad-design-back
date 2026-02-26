from django.db import models


class Catalog(models.Model):
    title = models.CharField(max_length=255)
    title_another_language = models.CharField(max_length=255)
    slug = models.SlugField(unique=True)
    descriptions = models.JSONField(default=list)

    def __str__(self):
        return self.title


class DarkPattern(models.Model):
    catalog = models.ForeignKey(
        Catalog,
        on_delete=models.CASCADE,
        related_name="dark_patterns"
    )

    title = models.CharField(max_length=255)
    title_another_language_for_list = models.CharField(max_length=255, blank=True)
    description_for_list = models.TextField(blank=True)
    descriptions = models.JSONField(default=list, blank=True)
    key_mechanics = models.JSONField(default=list, blank=True)
    key_mechanics_video = models.URLField(blank=True)
    consequences_for_the_user = models.JSONField(default=list, blank=True)
    alternatives = models.JSONField(default=list, blank=True)

    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ["order"]

    def __str__(self):
        return self.title
    
