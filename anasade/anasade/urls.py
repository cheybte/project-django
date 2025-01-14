from django.contrib import admin
from django.urls import path, include  # Assurez-vous d'importer 'include'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('app.urls')),  # Inclure les URLs définies dans 'app/urls.py'
]
