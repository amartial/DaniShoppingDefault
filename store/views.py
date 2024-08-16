from django.shortcuts import render, get_object_or_404
from .models import Product, Category

def store(request, category_slug=None):
    """ Verifie si un slug de categorie est fourni """
    categories = None
    products = None

    # Vérifie si un slug de catégorie est fourni
    if category_slug is not None:
        # Récupère la catégorie correspondante ou renvoie une erreur 404 si elle n'existe pas
        categories = get_object_or_404(Category, slug=category_slug)
        # Filtre les produits par catégorie et disponibilité
        products = Product.objects.filter(category=categories, is_available=True)
        product_count = products.count()
    else:
        products = Product.objects.all().filter(is_available=True)
        product_count = products.count()

    context = {
        'products': products,  # Liste des produits filtrés
        'product_count': product_count,  # Nombre de produits trouvés
    }

    # Rend le template 'store/store.html' avec le contexte
    return render(request, 'store/store.html', context)
