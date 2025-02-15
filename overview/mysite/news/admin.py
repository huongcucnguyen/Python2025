from django.contrib import admin # type: ignore
from . import models

admin.site.register(models.Reporter)
admin.site.register(models.Article)

