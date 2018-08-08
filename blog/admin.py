from django.contrib import admin

# Register your models here.
from . import models
from .models import Article
admin.site.register(Article)
