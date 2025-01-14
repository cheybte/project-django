from django.contrib import admin
from .models import Wilaya, Moughataa, Commune, ProductType, Product, PointOfSale

# Configuration de l'interface admin pour Wilaya
@admin.register(Wilaya)
class WilayaAdmin(admin.ModelAdmin):
    list_display = ('id', 'code', 'name')  # Colonnes affichées dans la liste
    search_fields = ('name', 'code')      # Champs pour la barre de recherche
    list_filter = ('code',)              # Filtres dans la barre latérale (facultatif)
    ordering = ('id',)                   # Ordre par défaut dans la liste

# Configuration de l'interface admin pour Moughataa
@admin.register(Moughataa)
class MoughataaAdmin(admin.ModelAdmin):
    list_display = ('id', 'code', 'label', 'wilaya')  # Colonnes affichées
    search_fields = ('label', 'code', 'wilaya__name')  # Recherche par nom de Wilaya et Moughataa
    list_filter = ('wilaya',)                         # Filtres par Wilaya
    ordering = ('id',)                                # Ordre par défaut


@admin.register(Commune)
class CommuneAdmin(admin.ModelAdmin):
    list_display = ('id', 'code', 'name', 'moughataa')
    search_fields = ('name', 'code', 'moughataa__label')
    
    
@admin.register(ProductType)
class ProductTypeAdmin(admin.ModelAdmin):
    list_display = ('id', 'code', 'label', 'description')
    search_fields = ('label', 'code')

    
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'code', 'name', 'unit_measure', 'product_type')
    search_fields = ('name', 'code')
    
    
@admin.register(PointOfSale)
class PointOfSaleAdmin(admin.ModelAdmin):
    list_display = ('id', 'code', 'type', 'gps_lat', 'gps_lon', 'commune')
    search_fields = ('code', 'type', 'commune__name')