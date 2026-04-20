from django.urls import path
from app.views.product_view import *
from app.views.category_view import *
from .views import *
app_name = 'products'

urlpatterns = [
    path('category-list/', category_list, name='category_list'),
    path('product-list/', product_list, name='product_list'),
    path('product-detail/<int:id>/', product_detail, name='product_detail'),
    path('category/<slug>/', category_products, name='category_products'),
    path('add/', product_upload, name='product_upload'),
]

