from django.contrib import admin
from django.contrib.admin import ModelAdmin

from articles import models


@admin.register(models.Article)
class ArticleAdmin(ModelAdmin):
    pass
