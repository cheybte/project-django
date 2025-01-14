from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.http import HttpResponse
from .models import Wilaya, Moughataa, Commune, ProductType, Product, PointOfSale, Cart, ProductPrice, CartProduct


# --- VUES POUR WILAYA ---
class WilayaCreateView(CreateView):
    model = Wilaya
    fields = ['code', 'name']
    template_name = 'wilaya/create.html'
    success_url = reverse_lazy('wilaya-list')


class WilayaListView(ListView):
    model = Wilaya
    template_name = 'wilaya/list.html'
    context_object_name = 'wilayas'


class WilayaUpdateView(UpdateView):
    model = Wilaya
    fields = ['code', 'name']
    template_name = 'wilaya/update.html'
    success_url = reverse_lazy('wilaya-list')


class WilayaDeleteView(DeleteView):
    model = Wilaya
    template_name = 'wilaya/delete.html'
    success_url = reverse_lazy('wilaya-list')


# --- VUES POUR MOUGHATAA ---
class MoughataaCreateView(CreateView):
    model = Moughataa
    fields = ['code', 'label', 'wilaya']
    template_name = 'moughataa/create.html'
    success_url = reverse_lazy('moughataa-list')


class MoughataaListView(ListView):
    model = Moughataa
    template_name = 'moughataa/list.html'
    context_object_name = 'moughataas'


class MoughataaUpdateView(UpdateView):
    model = Moughataa
    fields = ['code', 'label', 'wilaya']
    template_name = 'moughataa/update.html'
    success_url = reverse_lazy('moughataa-list')


class MoughataaDeleteView(DeleteView):
    model = Moughataa
    template_name = 'moughataa/delete.html'
    success_url = reverse_lazy('moughataa-list')


# --- VUES POUR COMMUNE ---
class CommuneListView(ListView):
    model = Commune
    template_name = 'commune/list.html'
    context_object_name = 'communes'


class CommuneCreateView(CreateView):
    model = Commune
    fields = ['code', 'name', 'moughataa']
    template_name = 'commune/create.html'
    success_url = reverse_lazy('commune-list')


class CommuneUpdateView(UpdateView):
    model = Commune
    fields = ['code', 'name', 'moughataa']
    template_name = 'commune/update.html'
    success_url = reverse_lazy('commune-list')


class CommuneDeleteView(DeleteView):
    model = Commune
    template_name = 'commune/delete.html'
    success_url = reverse_lazy('commune-list')


# --- VUES POUR PRODUCTTYPE ---
class ProductTypeListView(ListView):
    model = ProductType
    template_name = 'producttype/list.html'
    context_object_name = 'producttypes'


class ProductTypeCreateView(CreateView):
    model = ProductType
    fields = ['code', 'label', 'description']
    template_name = 'producttype/create.html'
    success_url = reverse_lazy('producttype-list')


class ProductTypeUpdateView(UpdateView):
    model = ProductType
    fields = ['code', 'label', 'description']
    template_name = 'producttype/update.html'
    success_url = reverse_lazy('producttype-list')


class ProductTypeDeleteView(DeleteView):
    model = ProductType
    template_name = 'producttype/delete.html'
    success_url = reverse_lazy('producttype-list')


# --- VUES POUR PRODUCT ---
class ProductListView(ListView):
    model = Product
    template_name = 'product/list.html'
    context_object_name = 'products'


class ProductCreateView(CreateView):
    model = Product
    fields = ['code', 'name', 'description', 'unit_measure', 'product_type']
    template_name = 'product/create.html'
    success_url = reverse_lazy('product-list')


class ProductUpdateView(UpdateView):
    model = Product
    fields = ['code', 'name', 'description', 'unit_measure', 'product_type']
    template_name = 'product/update.html'
    success_url = reverse_lazy('product-list')


class ProductDeleteView(DeleteView):
    model = Product
    template_name = 'product/delete.html'
    success_url = reverse_lazy('product-list')


# --- VUES POUR POINT OF SALE ---
class PointOfSaleListView(ListView):
    model = PointOfSale
    template_name = 'pointofsale/list.html'
    context_object_name = 'points_of_sale'


class PointOfSaleCreateView(CreateView):
    model = PointOfSale
    fields = ['code', 'type', 'gps_lat', 'gps_lon', 'commune']
    template_name = 'pointofsale/create.html'
    success_url = reverse_lazy('pointofsale-list')


class PointOfSaleUpdateView(UpdateView):
    model = PointOfSale
    fields = ['code', 'type', 'gps_lat', 'gps_lon', 'commune']
    template_name = 'pointofsale/update.html'
    success_url = reverse_lazy('pointofsale-list')


class PointOfSaleDeleteView(DeleteView):
    model = PointOfSale
    template_name = 'pointofsale/delete.html'
    success_url = reverse_lazy('pointofsale-list')


# --- VUES POUR CART ---
class CartListView(ListView):
    model = Cart
    template_name = 'cart/list.html'
    context_object_name = 'carts'


class CartCreateView(CreateView):
    model = Cart
    fields = ['code', 'name', 'description']
    template_name = 'cart/create.html'
    success_url = reverse_lazy('cart-list')


class CartUpdateView(UpdateView):
    model = Cart
    fields = ['code', 'name', 'description']
    template_name = 'cart/update.html'
    success_url = reverse_lazy('cart-list')


class CartDeleteView(DeleteView):
    model = Cart
    template_name = 'cart/delete.html'
    success_url = reverse_lazy('cart-list')

class ProductPriceListView(ListView):
    model = ProductPrice
    template_name = 'productprice/list.html'
    context_object_name = 'product_prices'


class ProductPriceCreateView(CreateView):
    model = ProductPrice
    fields = ['value', 'date_from', 'date_to', 'product', 'point_of_sale']
    template_name = 'productprice/create.html'
    success_url = reverse_lazy('productprice-list')


class ProductPriceUpdateView(UpdateView):
    model = ProductPrice
    fields = ['value', 'date_from', 'date_to', 'product', 'point_of_sale']
    template_name = 'productprice/update.html'
    success_url = reverse_lazy('productprice-list')


class ProductPriceDeleteView(DeleteView):
    model = ProductPrice
    template_name = 'productprice/delete.html'
    success_url = reverse_lazy('productprice-list')
    

# Liste des CartProducts
class CartProductListView(ListView):
    model = CartProduct
    template_name = 'cartproduct/list.html'
    context_object_name = 'cartproducts'

# Créer un CartProduct
class CartProductCreateView(CreateView):
    model = CartProduct
    fields = ['product', 'cart', 'weight', 'date_from', 'date_to']
    template_name = 'cartproduct/create.html'
    success_url = reverse_lazy('cartproduct-list')

# Modifier un CartProduct
class CartProductUpdateView(UpdateView):
    model = CartProduct
    fields = ['product', 'cart', 'weight', 'date_from', 'date_to']
    template_name = 'cartproduct/update.html'
    success_url = reverse_lazy('cartproduct-list')

# Supprimer un CartProduct
class CartProductDeleteView(DeleteView):
    model = CartProduct
    template_name = 'cartproduct/delete.html'
    success_url = reverse_lazy('cartproduct-list')



# --- PAGE D'ACCUEIL ---
def home(request):
    return HttpResponse("Bienvenue sur la page d'accueil.")
