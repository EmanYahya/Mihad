from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from app.models.cart import Cart, Order, OrderItem  
from app.forms.order_form import OrderForm  


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