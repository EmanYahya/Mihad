from django.db.models import Q
from django.shortcuts import render
from products.models import Product

def search(request):
    query = request.GET.get('q')
    results = []

    if query:
        # search by product name, brand name, category name, and description
        query_set = (
            Q(name__icontains=query) |
           # Q(brand__name__icontains=query) |
            Q(category__name__icontains=query) |
            Q(description__icontains=query)
        )

        # apply price filter if provided
        #if request.GET.get('min_price'):
        #    query_set &= Q(price__gte=request.GET['min_price'])
        #if request.GET.get('max_price'):
        #    query_set &= Q(price__lte=request.GET['max_price'])

        ## apply category filter if provided
        #if request.GET.get('category'):
        #    query_set &= Q(category__slug=request.GET['category'])

        ## apply sorting if provided
        #sorting = request.GET.get('sort')
        #if sorting == 'price_asc':
        #    results = Product.objects.filter(query_set).order_by('price')
        #elif sorting == 'price_desc':
        #    results = Product.objects.filter(query_set).order_by('-price')
        #elif sorting == 'name_asc':
        #    results = Product.objects.filter(query_set).order_by('name')
        #elif sorting == 'name_desc':
        #    results = Product.objects.filter(query_set).order_by('-name')
        #else:
        #    results = Product.objects.filter(query_set)
        products = Product.objects.filter(query_set)
    else:
        products = []

    return render(request, 'search.html', {
        'query': query,
        'results': results,
        'products': products,
    })

