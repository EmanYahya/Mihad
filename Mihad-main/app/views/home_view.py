from django.shortcuts import render
from products.models import Product, Category


def home(request):
    # Get featured products
    featured_products = Product.objects.filter(is_featured=True)

    # Get all categories
    categories = Category.objects.all()

    # Get popular products
    new_products = Product.objects.filter(is_newarrival=True)[:6]

    context = {
        'featured_products': featured_products,
        'categories': categories,
        'new_products': new_products
    }
    return render(request, 'home.html', context)

