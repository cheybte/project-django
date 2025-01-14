from django.db import models


# Modèle pour Wilaya
class Wilaya(models.Model):
    code = models.CharField(max_length=10, unique=True)  # Code unique de la Wilaya
    name = models.CharField(max_length=255)  # Nom de la Wilaya

    def __str__(self):
        return self.name  # Affiche le nom dans l'interface admin et ailleurs


# Modèle pour Moughataa
class Moughataa(models.Model):
    code = models.CharField(max_length=10, unique=True)  # Code unique de la Moughataa
    label = models.CharField(max_length=255)  # Nom ou label de la Moughataa
    wilaya = models.ForeignKey(Wilaya, on_delete=models.CASCADE, related_name="moughataas")  # Relation avec Wilaya

    def __str__(self):
        return self.label  # Affiche le label dans l'interface admin et ailleurs


# Modèle pour Commune
class Commune(models.Model):
    code = models.CharField(max_length=45, unique=True)  # Code unique
    name = models.CharField(max_length=45)  # Nom de la Commune
    moughataa = models.ForeignKey(Moughataa, on_delete=models.CASCADE, related_name="communes")  # Relation avec Moughataa

    def __str__(self):
        return self.name


# Modèle pour ProductType
class ProductType(models.Model):
    code = models.CharField(max_length=45, unique=True)  # Code unique
    label = models.CharField(max_length=100)  # Label ou nom du type de produit
    description = models.TextField(blank=True)  # Description (optionnel)

    def __str__(self):
        return self.label


# Modèle pour Product
class Product(models.Model):
    code = models.CharField(max_length=45, unique=True)  # Code unique
    name = models.CharField(max_length=100)  # Nom du produit
    description = models.TextField(blank=True)  # Description (optionnel)
    unit_measure = models.CharField(max_length=45)  # Unité de mesure (kg, litre, etc.)
    product_type = models.ForeignKey(ProductType, on_delete=models.CASCADE, related_name="products")  # Relation avec ProductType

    def __str__(self):
        return self.name


# Modèle pour PointOfSale
class PointOfSale(models.Model):
    code = models.CharField(max_length=45, unique=True)  # Code unique
    type = models.CharField(max_length=45)  # Type de point de vente (supermarché, magasin, etc.)
    gps_lat = models.FloatField()  # Latitude GPS
    gps_lon = models.FloatField()  # Longitude GPS
    commune = models.ForeignKey(Commune, on_delete=models.CASCADE, related_name="points_of_sale")  # Relation avec Commune

    def __str__(self):
        return f"{self.code} - {self.type}"


# Modèle pour Cart
class Cart(models.Model):
    code = models.CharField(max_length=45, unique=True)  # Code unique
    name = models.CharField(max_length=45)  # Nom du panier
    description = models.TextField(blank=True)  # Description (optionnel)

    def __str__(self):
        return self.name

class ProductPrice(models.Model):
    value = models.FloatField()  # Prix du produit
    date_from = models.DateField()  # Date de début
    date_to = models.DateField()  # Date de fin
    product = models.ForeignKey(Product, on_delete=models.CASCADE)  # Référence au produit
    point_of_sale = models.ForeignKey(PointOfSale, on_delete=models.CASCADE)  # Référence au point de vente

    def __str__(self):
        return f"{self.product.name} - {self.value}"
    
class CartProduct(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    weight = models.FloatField()
    date_from = models.DateField()
    date_to = models.DateField()

    def __str__(self):
        return f"{self.cart.name} - {self.product.name}"