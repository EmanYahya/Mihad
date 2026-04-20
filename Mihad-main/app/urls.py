from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views.home_view import *
from .views.category_view import *
from .views.product_view import *
from .views.cart_view import *
from .views.wishlist_view import *
from .views.search_view import *
from .views.account_view import *

app_name = 'app'

urlpatterns = [
    path('search/', search, name='search'),
    path('login/', login_view, name='login_view'),
    path('register/', register_view, name='register_view'),
    path('logout/', logout_view, name='logout_view'),
    path('cart/', cart_detail, name='cart_detail'),
    path('add-to-cart/<int:product_id>/', add_to_cart, name='add_to_cart'),
    path('remove-from-cart/<int:cart_item_id>/', remove_from_cart, name='remove_from_cart'),
    path('update-cart-item/<int:cart_item_id>/', update_cart_item, name='update_cart_item'),
    path('wishlist/', wishlist, name='wishlist'),
    path('add-to-wishlist/<int:product_id>/', add_to_wishlist, name='add_to_wishlist'),
    path('remove-from-wishlist/<int:product_id>/', remove_from_wishlist, name='remove_from_wishlist'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

