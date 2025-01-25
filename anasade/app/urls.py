from django.urls import path
from django.contrib.auth import views as auth_views
from django.contrib.auth.views import LoginView, LogoutView
from .views import (
    # Importation/Exportation
    import_wilayas, export_wilayas,
    import_moughataas, export_moughataas,
    import_communes, export_communes,
    import_carts, export_carts,
    import_cartproducts, export_cartproducts,
    import_products, export_products,
    import_pointofsales, export_pointofsales,
    import_productprices, export_productprices,
    import_producttypes, export_producttypes,
    calculer_inpc,

    # Vues pour les modèles
    WilayaListView, WilayaCreateView, WilayaUpdateView, WilayaDeleteView,
    MoughataaListView, MoughataaCreateView, MoughataaUpdateView, MoughataaDeleteView,
    CommuneListView, CommuneCreateView, CommuneUpdateView, CommuneDeleteView,
    ProductTypeListView, ProductTypeCreateView, ProductTypeUpdateView, ProductTypeDeleteView,
    ProductListView, ProductCreateView, ProductUpdateView, ProductDeleteView,
    PointOfSaleListView, PointOfSaleCreateView, PointOfSaleUpdateView, PointOfSaleDeleteView,
    CartListView, CartCreateView, CartUpdateView, CartDeleteView,
    ProductPriceListView, ProductPriceCreateView, ProductPriceUpdateView, ProductPriceDeleteView,
    CartProductListView, CartProductCreateView, CartProductUpdateView, CartProductDeleteView,

    # Page d'accueil
    home,
)

urlpatterns = [
    # Page d'accueil
    path('', home, name='home'),
    
    # Wilaya
    path('wilayas/', WilayaListView.as_view(), name='wilaya-list'),
    path('wilayas/create/', WilayaCreateView.as_view(), name='wilaya-create'),
    path('wilayas/<int:pk>/update/', WilayaUpdateView.as_view(), name='wilaya-update'),
    path('wilayas/<int:pk>/delete/', WilayaDeleteView.as_view(), name='wilaya-delete'),
    path('wilayas/import/', import_wilayas, name='wilaya-import'),
    path('wilayas/export/', export_wilayas, name='wilaya-export'),

    # Moughataa
    path('moughataas/', MoughataaListView.as_view(), name='moughataa-list'),
    path('moughataas/create/', MoughataaCreateView.as_view(), name='moughataa-create'),
    path('moughataas/<int:pk>/update/', MoughataaUpdateView.as_view(), name='moughataa-update'),
    path('moughataas/<int:pk>/delete/', MoughataaDeleteView.as_view(), name='moughataa-delete'),
    path('moughataas/import/', import_moughataas, name='moughataa-import'),
    path('moughataas/export/', export_moughataas, name='moughataa-export'),

    # Commune
    path('communes/', CommuneListView.as_view(), name='commune-list'),
    path('communes/create/', CommuneCreateView.as_view(), name='commune-create'),
    path('communes/<int:pk>/update/', CommuneUpdateView.as_view(), name='commune-update'),
    path('communes/<int:pk>/delete/', CommuneDeleteView.as_view(), name='commune-delete'),
    path('communes/import/', import_communes, name='commune-import'),
    path('communes/export/', export_communes, name='commune-export'),

    # ProductType
    path('producttypes/', ProductTypeListView.as_view(), name='producttype-list'),
    path('producttypes/create/', ProductTypeCreateView.as_view(), name='producttype-create'),
    path('producttypes/<int:pk>/update/', ProductTypeUpdateView.as_view(), name='producttype-update'),
    path('producttypes/<int:pk>/delete/', ProductTypeDeleteView.as_view(), name='producttype-delete'),
    path('producttypes/import/', import_producttypes, name='producttype-import'),
    path('producttypes/export/', export_producttypes, name='producttype-export'),

    # Product
    path('products/', ProductListView.as_view(), name='product-list'),
    path('products/create/', ProductCreateView.as_view(), name='product-create'),
    path('products/<int:pk>/update/', ProductUpdateView.as_view(), name='product-update'),
    path('products/<int:pk>/delete/', ProductDeleteView.as_view(), name='product-delete'),
    path('products/import/', import_products, name='product-import'),
    path('products/export/', export_products, name='product-export'),

    # PointOfSale
    path('pointsofsale/', PointOfSaleListView.as_view(), name='pointofsale-list'),
    path('pointsofsale/create/', PointOfSaleCreateView.as_view(), name='pointofsale-create'),
    path('pointsofsale/<int:pk>/update/', PointOfSaleUpdateView.as_view(), name='pointofsale-update'),
    path('pointsofsale/<int:pk>/delete/', PointOfSaleDeleteView.as_view(), name='pointofsale-delete'),
    path('pointsofsale/import/', import_pointofsales, name='pointofsale-import'),
    path('pointsofsale/export/', export_pointofsales, name='pointofsale-export'),

    # Cart
    path('carts/', CartListView.as_view(), name='cart-list'),
    path('carts/create/', CartCreateView.as_view(), name='cart-create'),
    path('carts/<int:pk>/update/', CartUpdateView.as_view(), name='cart-update'),
    path('carts/<int:pk>/delete/', CartDeleteView.as_view(), name='cart-delete'),
    path('carts/import/', import_carts, name='cart-import'),
    path('carts/export/', export_carts, name='cart-export'),

    # CartProduct
    path('cartproducts/', CartProductListView.as_view(), name='cartproduct-list'),
    path('cartproducts/create/', CartProductCreateView.as_view(), name='cartproduct-create'),
    path('cartproducts/<int:pk>/update/', CartProductUpdateView.as_view(), name='cartproduct-update'),
    path('cartproducts/<int:pk>/delete/', CartProductDeleteView.as_view(), name='cartproduct-delete'),
    path('cartproducts/import/', import_cartproducts, name='cartproduct-import'),
    path('cartproducts/export/', export_cartproducts, name='cartproduct-export'),

    # ProductPrice
    path('productprices/', ProductPriceListView.as_view(), name='productprice-list'),
    path('productprices/create/', ProductPriceCreateView.as_view(), name='productprice-create'),
    path('productprices/<int:pk>/update/', ProductPriceUpdateView.as_view(), name='productprice-update'),
    path('productprices/<int:pk>/delete/', ProductPriceDeleteView.as_view(), name='productprice-delete'),
    path('productprices/import/', import_productprices, name='productprice-import'),
    path('productprices/export/', export_productprices, name='productprice-export'),

    # INPC
    path('inpc/', calculer_inpc, name='calculate-inpc'),
    
    path('login/', LoginView.as_view(template_name='login.html'), name='login'),  # Page de connexion
    path('logout/', LogoutView.as_view(), name='logout'),

]
