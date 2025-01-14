from django.urls import path
from .views import (
    # Wilayas
    WilayaCreateView, WilayaListView, WilayaUpdateView, WilayaDeleteView,
    
    # Moughataas
    MoughataaCreateView, MoughataaListView, MoughataaUpdateView, MoughataaDeleteView,
    
    # Communes
    CommuneListView, CommuneCreateView, CommuneUpdateView, CommuneDeleteView,
    
    # Product Types
    ProductTypeListView, ProductTypeCreateView, ProductTypeUpdateView, ProductTypeDeleteView,
    
    # Products
    ProductListView, ProductCreateView, ProductUpdateView, ProductDeleteView,
    
    # Points of Sale
    PointOfSaleListView, PointOfSaleCreateView, PointOfSaleUpdateView, PointOfSaleDeleteView,
    
    # Carts
    CartListView, CartCreateView, CartUpdateView, CartDeleteView,
    
    # Product Prices
    ProductPriceListView, ProductPriceCreateView, ProductPriceUpdateView, ProductPriceDeleteView,

    CartProductListView, CartProductCreateView, CartProductUpdateView, CartProductDeleteView,
    # Home
    home,
)

urlpatterns = [
    # Routes pour Wilaya
    path('wilayas/', WilayaListView.as_view(), name='wilaya-list'),
    path('wilayas/new/', WilayaCreateView.as_view(), name='wilaya-create'),
    path('wilayas/<int:pk>/edit/', WilayaUpdateView.as_view(), name='wilaya-update'),
    path('wilayas/<int:pk>/delete/', WilayaDeleteView.as_view(), name='wilaya-delete'),

    # Routes pour Moughataa
    path('moughataas/', MoughataaListView.as_view(), name='moughataa-list'),
    path('moughataas/new/', MoughataaCreateView.as_view(), name='moughataa-create'),
    path('moughataas/<int:pk>/edit/', MoughataaUpdateView.as_view(), name='moughataa-update'),
    path('moughataas/<int:pk>/delete/', MoughataaDeleteView.as_view(), name='moughataa-delete'),

    # Routes pour Commune
    path('communes/', CommuneListView.as_view(), name='commune-list'),
    path('communes/new/', CommuneCreateView.as_view(), name='commune-create'),
    path('communes/<int:pk>/edit/', CommuneUpdateView.as_view(), name='commune-update'),
    path('communes/<int:pk>/delete/', CommuneDeleteView.as_view(), name='commune-delete'),
    
    # Routes pour ProductType
    path('producttypes/', ProductTypeListView.as_view(), name='producttype-list'),
    path('producttypes/new/', ProductTypeCreateView.as_view(), name='producttype-create'),
    path('producttypes/<int:pk>/edit/', ProductTypeUpdateView.as_view(), name='producttype-update'),
    path('producttypes/<int:pk>/delete/', ProductTypeDeleteView.as_view(), name='producttype-delete'),

    # Routes pour Product
    path('products/', ProductListView.as_view(), name='product-list'),
    path('products/new/', ProductCreateView.as_view(), name='product-create'),
    path('products/<int:pk>/edit/', ProductUpdateView.as_view(), name='product-update'),
    path('products/<int:pk>/delete/', ProductDeleteView.as_view(), name='product-delete'),

    # Routes pour Point of Sale
    path('pointsofsale/', PointOfSaleListView.as_view(), name='pointofsale-list'),
    path('pointsofsale/new/', PointOfSaleCreateView.as_view(), name='pointofsale-create'),
    path('pointsofsale/<int:pk>/edit/', PointOfSaleUpdateView.as_view(), name='pointofsale-update'),
    path('pointsofsale/<int:pk>/delete/', PointOfSaleDeleteView.as_view(), name='pointofsale-delete'),
    
    # Routes pour Cart
    path('carts/', CartListView.as_view(), name='cart-list'),
    path('carts/new/', CartCreateView.as_view(), name='cart-create'),
    path('carts/<int:pk>/edit/', CartUpdateView.as_view(), name='cart-update'),
    path('carts/<int:pk>/delete/', CartDeleteView.as_view(), name='cart-delete'),
    
    # Routes pour ProductPrice
    path('productprices/', ProductPriceListView.as_view(), name='productprice-list'),
    path('productprices/new/', ProductPriceCreateView.as_view(), name='productprice-create'),
    path('productprices/<int:pk>/edit/', ProductPriceUpdateView.as_view(), name='productprice-update'),
    path('productprices/<int:pk>/delete/', ProductPriceDeleteView.as_view(), name='productprice-delete'),

    
    path('cartproducts/', CartProductListView.as_view(), name='cartproduct-list'),
    path('cartproducts/new/', CartProductCreateView.as_view(), name='cartproduct-create'),
    path('cartproducts/<int:pk>/edit/', CartProductUpdateView.as_view(), name='cartproduct-update'),
    path('cartproducts/<int:pk>/delete/', CartProductDeleteView.as_view(), name='cartproduct-delete'),

    # Page d'accueil
    path('home/', home, name='home'),
]
