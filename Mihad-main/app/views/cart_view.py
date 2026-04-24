from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from app.models.cart import Cart, Order, OrderItem  
from app.forms.order_form import OrderForm  

@login_required
def update_cart_item(request, cart_item_id):
    cart_item = get_object_or_404(Cart, id=cart_item_id, user=request.user)
    if request.method == 'POST':
        quantity = int(request.POST.get('quantity', 1))
        if quantity > 0:
            cart_item.quantity = quantity
            cart_item.save()
    return redirect('app:cart_detail')

@login_required
def add_to_cart(request, product_id):
    # جلب المنتج أو إظهار 404 لو مش موجود
    # ملحوظة: تأكدي إن اسم الموديل Product وليس Products
    from ..models import Product 
    product = get_object_or_404(Product, id=product_id)
    
    # البحث عن المنتج في عربة المستخدم أو إنشاؤه
    cart_item, created = Cart.objects.get_or_create(
        user=request.user, 
        product=product
    )
    
    if not created:
        cart_item.quantity += 1
        cart_item.save()
        
    return redirect('app:cart_detail')

@login_required
def cart_detail(request):
    # جلب كل العناصر الموجودة في سلة المستخدم الحالي
    cart_items = Cart.objects.filter(user=request.user)
    
    # حساب إجمالي السعر لكل المنتجات في السلة
    total_price = sum(item.product.price * item.quantity for item in cart_items)
    
    context = {
        'cart_items': cart_items,
        'total_price': total_price,
    }
    return render(request, 'app/cart_detail.html', context)

@login_required
def remove_from_cart(request, cart_item_id):
    # جلب عنصر العربة وحذفه
    cart_item = get_object_or_404(Cart, id=cart_item_id, user=request.user)
    cart_item.delete()
    return redirect('app:cart_detail')

@login_required
def checkout(request):
    # جلب عناصر السلة للمستخدم الحالي
    cart_items = Cart.objects.filter(user=request.user)
    
    if not cart_items:
        return redirect('app:cart_detail')

    # حساب إجمالي السعر
    total_price = sum(item.product.price * item.quantity for item in cart_items)

    if request.method == 'POST':
        form = OrderForm(request.POST) # استخدام الفورم الخاصة بكِ
        if form.is_valid():
            # حفظ الأوردر مبدئياً لإضافة البيانات التلقائية
            order = form.save(commit=False)
            order.user = request.user
            order.total_price = total_price
            order.save()

            # تحويل كل منتج في السلة إلى OrderItem
            for item in cart_items:
                OrderItem.objects.create(
                    order=order,
                    product=item.product,
                    price=item.product.price,
                    quantity=item.quantity
                )
            
            # مسح السلة بعد نجاح الطلب
            cart_items.delete()

            return render(request, 'app/order_success.html', {'order': order})
    else:
        form = OrderForm()

    return render(request, 'app/checkout.html', {'form': form, 'total': total_price})