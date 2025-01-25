from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.http import HttpResponse
from .models import Wilaya, Moughataa, Commune, ProductType, Product, PointOfSale, Cart, ProductPrice, CartProduct

from django.shortcuts import render, redirect
from django.contrib import messages
import pandas as pd




def import_wilayas(request):
    if request.method == 'POST':
        excel_file = request.FILES.get('file')
        if not excel_file:
            messages.error(request, "Veuillez sélectionner un fichier Excel.")
            return redirect('wilaya-list')

        try:
            df = pd.read_excel(excel_file)
            if not set(['code', 'name']).issubset(df.columns):
                messages.error(request, "Le fichier Excel doit contenir les colonnes 'code' et 'name'.")
                return redirect('wilaya-list')
            Wilaya.objects.all().delete()
            for _, row in df.iterrows():
                Wilaya.objects.create(code=row['code'], name=row['name'])
            messages.success(request, "Les données ont été importées avec succès.")
        except Exception as e:
            messages.error(request, f"Erreur lors de l'importation : {e}")
        return redirect('wilaya-list')
    return render(request, 'wilaya/import.html')
    
def import_moughataas(request):
    if request.method == 'POST':
        excel_file = request.FILES.get('file')
        if not excel_file:
            messages.error(request, "Veuillez sélectionner un fichier Excel.")
            return redirect('moughataa-list')

        try:
            df = pd.read_excel(excel_file)
            if not set(['code', 'label', 'wilaya_id']).issubset(df.columns):
                messages.error(request, "Le fichier Excel doit contenir les colonnes 'code', 'label' et 'wilaya_id'.")
                return redirect('moughataa-list')
            Moughataa.objects.all().delete()
            for _, row in df.iterrows():
                Moughataa.objects.create(code=row['code'], label=row['label'], wilaya_id=row['wilaya_id'])
            messages.success(request, "Les données ont été importées avec succès.")
        except Exception as e:
            messages.error(request, f"Erreur lors de l'importation : {e}")
        return redirect('moughataa-list')
    return render(request, 'moughataa/import.html')

def import_communes(request):
    if request.method == 'POST':
        excel_file = request.FILES.get('file')
        if not excel_file:
            messages.error(request, "Veuillez sélectionner un fichier Excel.")
            return redirect('commune-list')

        try:
            df = pd.read_excel(excel_file)
            if not set(['code', 'name', 'moughataa_id']).issubset(df.columns):
                messages.error(request, "Le fichier Excel doit contenir les colonnes 'code', 'name' et 'moughataa_id'.")
                return redirect('commune-list')
            Commune.objects.all().delete()
            for _, row in df.iterrows():
                Commune.objects.create(code=row['code'], name=row['name'], moughataa_id=row['moughataa_id'])
            messages.success(request, "Les données ont été importées avec succès.")
        except Exception as e:
            messages.error(request, f"Erreur lors de l'importation : {e}")
        return redirect('commune-list')
    return render(request, 'commune/import.html')

def import_carts(request):
    if request.method == 'POST':
        excel_file = request.FILES.get('file')
        if not excel_file:
            messages.error(request, "Veuillez sélectionner un fichier Excel.")
            return redirect('cart-list')

        try:
            df = pd.read_excel(excel_file)
            if not set(['code', 'name', 'description']).issubset(df.columns):
                messages.error(request, "Le fichier Excel doit contenir les colonnes 'code', 'name' et 'description'.")
                return redirect('cart-list')
            Cart.objects.all().delete()
            for _, row in df.iterrows():
                Cart.objects.create(code=row['code'], name=row['name'], description=row['description'])
            messages.success(request, "Les données ont été importées avec succès.")
        except Exception as e:
            messages.error(request, f"Erreur lors de l'importation : {e}")
        return redirect('cart-list')
    return render(request, 'cart/import.html')

def import_cartproducts(request):
    if request.method == 'POST':
        excel_file = request.FILES.get('file')
        if not excel_file:
            messages.error(request, "Veuillez sélectionner un fichier Excel.")
            return redirect('cartproduct-list')

        try:
            # Charger le fichier Excel
            df = pd.read_excel(excel_file)

            # Vérifier les colonnes nécessaires
            required_columns = ['product_code', 'cart_code', 'weight', 'date_from', 'date_to']
            if not set(required_columns).issubset(df.columns):
                messages.error(request, f"Le fichier Excel doit contenir les colonnes {', '.join(required_columns)}.")
                return redirect('cartproduct-list')

            # Supprimer toutes les entrées existantes (si nécessaire)
            CartProduct.objects.all().delete()

            # Parcourir chaque ligne du fichier pour importer les données
            for _, row in df.iterrows():
                # Valider les relations avec Product et Cart
                try:
                    product = Product.objects.get(code=row['product_code'])
                    cart = Cart.objects.get(code=row['cart_code'])
                except Product.DoesNotExist:
                    messages.error(request, f"Produit avec le code '{row['product_code']}' introuvable.")
                    continue
                except Cart.DoesNotExist:
                    messages.error(request, f"Panier avec le code '{row['cart_code']}' introuvable.")
                    continue

                # Créer un CartProduct
                CartProduct.objects.create(
                    product=product,
                    cart=cart,
                    weight=row['weight'],
                    date_from=row['date_from'],
                    date_to=row['date_to']
                )

            messages.success(request, "Les données ont été importées avec succès.")
        except Exception as e:
            messages.error(request, f"Erreur lors de l'importation : {e}")

        return redirect('cartproduct-list')

    return render(request, 'cartproduct/import.html')

def import_products(request):
    if request.method == 'POST':
        excel_file = request.FILES.get('file')

        if not excel_file:
            messages.error(request, "Veuillez sélectionner un fichier Excel.")
            return redirect('product-import')

        if not excel_file.name.endswith(('.xls', '.xlsx')):
            messages.error(request, "Veuillez importer un fichier Excel valide (extension .xls ou .xlsx).")
            return redirect('product-import')

        try:
            # Charger le fichier Excel
            df = pd.read_excel(excel_file)

            # Vérifier les colonnes nécessaires
            if not set(['code', 'name', 'description', 'unit_measure', 'product_type']).issubset(df.columns):
                messages.error(request, "Le fichier Excel doit contenir les colonnes 'code', 'name', 'description', 'unit_measure', et 'product_type'.")
                return redirect('product-import')

            # Importer ou mettre à jour les données
            for _, row in df.iterrows():
                if pd.isnull(row['code']) or pd.isnull(row['name']) or pd.isnull(row['unit_measure']):
                    messages.error(request, "Le fichier contient des lignes avec des données manquantes.")
                    return redirect('product-import')

                # Récupérer ou créer le ProductType
                product_type, created = ProductType.objects.get_or_create(
                    label=row['product_type'],
                    defaults={
                        'description': 'Auto-created from import'  # Valeur par défaut si non existant
                    }
                )

                # Créer ou mettre à jour le produit
                Product.objects.update_or_create(
                    code=row['code'],
                    defaults={
                        'name': row['name'],
                        'description': row.get('description', ''),
                        'unit_measure': row['unit_measure'],
                        'product_type': product_type,
                    }
                )

            messages.success(request, "Les produits ont été importés avec succès.")

        except Exception as e:
            messages.error(request, f"Erreur lors de l'importation : {e}")

        return redirect('product-list')

    return render(request, 'product/import.html')



def import_pointofsales(request):
    if request.method == 'POST':
        excel_file = request.FILES.get('file')

        if not excel_file:
            messages.error(request, "Veuillez sélectionner un fichier Excel.")
            return redirect('pointofsale-import')

        if not excel_file.name.endswith(('.xls', '.xlsx')):
            messages.error(request, "Veuillez importer un fichier Excel valide (extension .xls ou .xlsx).")
            return redirect('pointofsale-import')

        try:
            # Charger le fichier Excel avec pandas
            df = pd.read_excel(excel_file)

            # Vérifier les colonnes nécessaires
            required_columns = {'code', 'type', 'gps_lat', 'gps_lon', 'commune_code'}
            if not required_columns.issubset(df.columns):
                messages.error(request, f"Le fichier Excel doit contenir les colonnes {', '.join(required_columns)}.")
                return redirect('pointofsale-import')

            # Importer ou mettre à jour les données
            for _, row in df.iterrows():
                if pd.isnull(row['code']) or pd.isnull(row['type']) or pd.isnull(row['commune_code']):
                    messages.error(request, "Le fichier contient des lignes avec des données manquantes.")
                    return redirect('pointofsale-import')

                try:
                    # Récupérer la commune associée
                    commune = Commune.objects.get(code=row['commune_code'])

                    # Créer ou mettre à jour le point de vente
                    PointOfSale.objects.update_or_create(
                        code=row['code'],
                        defaults={
                            'type': row['type'],
                            'gps_lat': row['gps_lat'],
                            'gps_lon': row['gps_lon'],
                            'commune': commune
                        }
                    )
                except Commune.DoesNotExist:
                    messages.error(request, f"Commune avec le code '{row['commune_code']}' introuvable.")
                    return redirect('pointofsale-import')

            messages.success(request, "Les points de vente ont été importés avec succès.")

        except Exception as e:
            messages.error(request, f"Erreur lors de l'importation : {e}")

        return redirect('pointofsale-list')

    return render(request, 'pointofsale/import.html')


def import_productprices(request):
    if request.method == 'POST':
        excel_file = request.FILES.get('file')

        if not excel_file:
            messages.error(request, "Veuillez sélectionner un fichier Excel.")
            return redirect('productprice-import')

        if not excel_file.name.endswith(('.xls', '.xlsx')):
            messages.error(request, "Veuillez importer un fichier Excel valide (extension .xls ou .xlsx).")
            return redirect('productprice-import')

        try:
            # Charger le fichier Excel
            df = pd.read_excel(excel_file)

            # Vérifier les colonnes nécessaires
            required_columns = ['product_code', 'point_of_sale_code', 'value', 'date_from', 'date_to']
            if not set(required_columns).issubset(df.columns):
                messages.error(request, f"Le fichier Excel doit contenir les colonnes : {', '.join(required_columns)}.")
                return redirect('productprice-import')

            # Importer ou mettre à jour les données
            for _, row in df.iterrows():
                # Vérifier les données obligatoires
                if pd.isnull(row['product_code']) or pd.isnull(row['point_of_sale_code']) or pd.isnull(row['value']):
                    messages.error(request, "Le fichier contient des lignes avec des données manquantes.")
                    return redirect('productprice-import')

                # Trouver le produit
                product = Product.objects.filter(code=row['product_code']).first()
                if not product:
                    messages.error(request, f"Le produit avec le code {row['product_code']} n'existe pas.")
                    continue

                # Trouver le point de vente
                point_of_sale = PointOfSale.objects.filter(code=row['point_of_sale_code']).first()
                if not point_of_sale:
                    messages.error(request, f"Le point de vente avec le code {row['point_of_sale_code']} n'existe pas.")
                    continue

                # Créer ou mettre à jour l'enregistrement ProductPrice
                ProductPrice.objects.create(
                    product=product,
                    point_of_sale=point_of_sale,
                    value=row['value'],
                    date_from=row['date_from'],
                    date_to=row['date_to']
                )

            messages.success(request, "Les prix des produits ont été importés avec succès.")

        except Exception as e:
            messages.error(request, f"Erreur lors de l'importation : {e}")

        return redirect('productprice-list')

    return render(request, 'productprice/import.html')





def import_producttypes(request):
    if request.method == 'POST':
        excel_file = request.FILES.get('file')

        if not excel_file:
            messages.error(request, "Veuillez sélectionner un fichier Excel.")
            return redirect('producttypes-import')

        if not excel_file.name.endswith(('.xls', '.xlsx')):
            messages.error(request, "Veuillez importer un fichier Excel valide (extension .xls ou .xlsx).")
            return redirect('producttypes-import')

        try:
            # Charger le fichier Excel
            df = pd.read_excel(excel_file)

            # Vérifier les colonnes nécessaires
            if not set(['code', 'label', 'description']).issubset(df.columns):
                messages.error(request, "Le fichier Excel doit contenir les colonnes 'code', 'label' et 'description'.")
                return redirect('producttypes-import')

            # Importer ou mettre à jour les données
            for _, row in df.iterrows():
                if pd.isnull(row['code']) or pd.isnull(row['label']):
                    messages.error(request, "Le fichier contient des lignes avec des données manquantes.")
                    return redirect('producttypes-import')

                ProductType.objects.update_or_create(
                    code=row['code'],
                    defaults={
                        'label': row['label'],
                        'description': row.get('description', ''),
                    }
                )

            messages.success(request, "Les ProductTypes ont été importés avec succès.")

        except Exception as e:
            messages.error(request, f"Erreur lors de l'importation : {e}")

        return redirect('producttype-list')

    return render(request, 'producttype/import.html')





def import_data(request, model, expected_columns, success_url, template_name):
    if request.method == 'POST':
        excel_file = request.FILES.get('file')
        if not excel_file:
            messages.error(request, "Veuillez sélectionner un fichier Excel.")
            return redirect(success_url)

        try:
            df = pd.read_excel(excel_file)
            if not set(expected_columns).issubset(df.columns):
                messages.error(request, f"Le fichier Excel doit contenir les colonnes {', '.join(expected_columns)}.")
                return redirect(success_url)
            model.objects.all().delete()
            for _, row in df.iterrows():
                model.objects.create(**{col: row[col] for col in expected_columns})
            messages.success(request, "Les données ont été importées avec succès.")
        except Exception as e:
            messages.error(request, f"Erreur lors de l'importation : {e}")
        return redirect(success_url)
    return render(request, template_name)


import openpyxl


def export_data(request, model, filename, fields):
    response = HttpResponse(
        content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet',
    )
    response['Content-Disposition'] = f'attachment; filename={filename}.xlsx'

    workbook = openpyxl.Workbook()
    sheet = workbook.active
    sheet.title = filename

    # Ajouter les en-têtes
    for idx, field in enumerate(fields, start=1):
        sheet.cell(row=1, column=idx, value=field)

    # Ajouter les données
    for row_idx, obj in enumerate(model.objects.all(), start=2):
        for col_idx, field in enumerate(fields, start=1):
            sheet.cell(row=row_idx, column=col_idx, value=getattr(obj, field))

    workbook.save(response)
    return response

def export_wilayas(request):
    return export_data(
        request,
        model=Wilaya,
        filename='wilayas',
        fields=['code', 'name']
    )

def export_moughataas(request):
    return export_data(
        request,
        model=Moughataa,
        filename='moughataas',
        fields=['code', 'label', 'wilaya__name']  # wilaya__name pour inclure le nom de la Wilaya associée
    )

def export_communes(request):
    return export_data(
        request,
        model=Commune,
        filename='communes',
        fields=['code', 'name', 'moughataa__label', 'moughataa__wilaya__name']  # Inclure les relations avec Moughataa et Wilaya
    )

def export_carts(request):
    return export_data(
        request,
        model=Cart,
        filename='carts',
        fields=['code', 'name', 'description']  # Colonnes à inclure dans l'export
    )
    
def export_cartproducts(request):
    return export_data(
        request,
        model=CartProduct,
        filename='cartproducts',
        fields=['cart__name', 'product__name', 'weight', 'date_from', 'date_to']
    )

def export_products(request):
    return export_data(
        request,
        model=Product,
        filename='products',
        fields=['code', 'name', 'description', 'unit_measure', 'product_type__label']
    )

def export_pointofsales(request):
    return export_data(
        request,
        model=PointOfSale,
        filename='points_of_sale',
        fields=['code', 'type', 'gps_lat', 'gps_lon', 'commune__name']
    )



def export_productprices(request):
    return export_data(
        request,
        model=ProductPrice,
        filename='product_prices',
        fields=['value', 'date_from', 'date_to', 'product__name', 'point_of_sale__code']
    )





def export_producttypes(request):
    return export_data(
        request,
        model=ProductType,
        filename='product_types',
        fields=['code', 'label', 'description']  # Colonnes exportées
    )


import matplotlib.pyplot as plt
from io import BytesIO
import base64



from django.db.models import Avg
from datetime import datetime
from django.shortcuts import render
from app.models import ProductType, Product, ProductPrice, CartProduct

from django.db.models import Avg
from django.shortcuts import render
from datetime import datetime
from app.models import ProductType, Product, ProductPrice, CartProduct

from calendar import month_name

def calculer_inpc(request):
    """
    Calcule l'Indice National des Prix à la Consommation (INPC)
    avec possibilité de sélectionner l'année et le mois.
    """
    # Année de base
    ANNEE_BASE = 2019

    # Récupérer l'année et le mois à partir de la requête, sinon utiliser l'année et le mois actuels
    annee_courante = request.GET.get('annee', datetime.now().year)
    mois_courant = request.GET.get('mois', datetime.now().month)

    try:
        annee_courante = int(annee_courante)
        mois_courant = int(mois_courant)
    except ValueError:
        annee_courante = datetime.now().year
        mois_courant = datetime.now().month

    # Récupérer tous les types de produits
    types_produits = ProductType.objects.all()

    # Dictionnaires pour stocker les résultats
    inpc_par_groupe = []
    inpc_global = {}

    # Calculer l'INPC pour chaque type de produit
    for type_produit in types_produits:
        # Récupérer les produits de ce type
        produits = Product.objects.filter(product_type=type_produit)

        # Variables pour les totaux
        prix_total_base = 0
        prix_total_courant = 0
        poids_total = 0
        produits_calcules = 0

        for produit in produits:
            # Récupérer les prix pour l'année de base
            prix_base = ProductPrice.objects.filter(
                product=produit,
                date_from__year=ANNEE_BASE,
                date_from__month=mois_courant
            ).order_by('-date_from').first()

            # Récupérer les prix pour l'année courante
            prix_courant = ProductPrice.objects.filter(
                product=produit,
                date_from__year=annee_courante,
                date_from__month=mois_courant
            ).order_by('-date_from').first()

            # Récupérer le poids du produit dans les paniers
            cart_products = CartProduct.objects.filter(
                product=produit,
                date_from__year__lte=annee_courante,  # Correction ici
                date_to__year__gte=annee_courante     # Correction ici
            )

            # Vérifier que tous les éléments nécessaires sont présents
            if prix_base and prix_courant and cart_products.exists():
                poids_moyen = cart_products.aggregate(Avg('weight'))['weight__avg'] or 0

                if poids_moyen > 0:
                    prix_total_base += prix_base.value * poids_moyen
                    prix_total_courant += prix_courant.value * poids_moyen
                    poids_total += poids_moyen
                    produits_calcules += 1

        # Calculer l'INPC pour ce groupe
        inpc_groupe = (prix_total_courant / prix_total_base * 100) if prix_total_base > 0 else 0

        # Ajouter les données du groupe si des produits sont calculés
        if produits_calcules > 0:
            inpc_par_groupe.append({
                'Année': annee_courante,
                'Mois': mois_courant,
                'Groupe': type_produit.label,
                'INPC': inpc_groupe,
                'Produits Calculés': produits_calcules
            })

    # Calculer l'INPC global
    inpc_total = sum(groupe['INPC'] for groupe in inpc_par_groupe) / len(inpc_par_groupe) if inpc_par_groupe else 0
    inpc_global[(annee_courante, mois_courant)] = inpc_total

    # Préparer les options d'années pour le formulaire
    annees_disponibles = sorted(set(
        ProductPrice.objects.values_list('date_from__year', flat=True).distinct()
    ))

    context = {
        'annee_base': ANNEE_BASE,
        'annee_courante': annee_courante,
        'mois_courant': mois_courant,
        'annees_disponibles': annees_disponibles,
        'inpc_par_groupe': inpc_par_groupe,
        'inpc_global': inpc_global
    }

    return render(request, 'inpc.html', context)





















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

from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render

@login_required




def home(request):
    return render(request, 'home.html')  # Rend le fichier 'home.html'