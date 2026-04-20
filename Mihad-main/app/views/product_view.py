from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db.models import Q
from django.views.generic import ListView

from products.models import Product, Review, Category
# from ..models.order import Order
from products.forms import ReviewForm


def product_list(request):
    """
    View function for product list page.
    Displays all the products in the database.
    """

    # Get all the products
    products = Product.objects.all()

    context = {'products': products}

    return render(request, 'product_list.html', context)


def product_detail(request, id):
    """
    View function for product detail page.
    Displays detailed information about a specific product.
    """

    # Get the product with the given id
    product = get_object_or_404(Product, id=id)

    # Get the related products (products in the same category)
    related_products = Product.objects.filter(category=product.category).exclude(id=id)

    context = {'product': product,
               'related_products': related_products,
             }

    return render(request, 'product_detail.html', context)

class ProductListView(ListView):
    model = Product
    template_name = 'product_list.html'
    paginate_by = 12


def category_products(request, slug):
    category = Category.objects.get(slug=slug)
    products = Product.objects.filter(category=category)
    query = request.GET.get('q')
    if query:
        products = products.filter(Q(name__icontains=query) | Q(description__icontains=query))
    context = {
        'category': category,
        'products': products
    }
    return render(request, 'category_products.html', context)
