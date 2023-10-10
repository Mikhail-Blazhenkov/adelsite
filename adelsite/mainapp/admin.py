from django.contrib import admin
from .models import PortfolioItem

class PortfolioItemAdmin(admin.ModelAdmin):
    list_display = ('name',)  # Отображать имя в административной панели

admin.site.register(PortfolioItem, PortfolioItemAdmin)

