from django.shortcuts import render, get_object_or_404

from carts.models import CartItem
from carts.views import _cart_id
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

def product_detail(request, category_slug, product_slug):
    try:
        single_product = Product.objects.get(category__slug=category_slug, slug=product_slug)
        in_cart = CartItem.objects.filter(cart__cart_id=_cart_id(request), product=single_product)
    except Exception as e:
        raise e

    context = {
        'single_product': single_product,
        'in_cart': in_cart,
    }
    return render(request, 'store/product_detail.html', context)
