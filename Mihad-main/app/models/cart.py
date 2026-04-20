from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
from products.models import Product  

# 1. جدول السلة (لحفظ المنتجات مؤقتاً)
class Cart(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.product.name}"

ADDRESS_CHOICES = (
    ('Home', 'المنزل'),
    ('Office', 'العمل'),
)

# 2. جدول الطلبات (لحفظ البيانات بعد إتمام الشراء)
class Order(models.Model):
    STATUS_CHOICES = (
        ('Pending', 'قيد الانتظار'),
        ('Shipped', 'تم الشحن'),
        ('Delivered', 'تم التوصيل'),
        ('Cancelled', 'تم الإلغاء'),
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="العميل")
    full_name = models.CharField(max_length=100, verbose_name="الاسم بالكامل")
    email = models.EmailField(verbose_name="البريد الإلكتروني")
    phone = models.CharField(max_length=20, verbose_name="رقم الهاتف")
    address = models.TextField(verbose_name="عنوان الشحن")
    city = models.CharField(max_length=50, verbose_name="المدينة")
    total_price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="إجمالي السعر")
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Pending', verbose_name="حالة الطلب")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="تاريخ الطلب")
    updated_at = models.DateTimeField(auto_now=True)
    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"Order {self.id} by {self.user.username}"

# 3. تفاصيل الطلب (المنتجات داخل كل طلب)
class OrderItem(models.Model):
    order = models.ForeignKey(Order, related_name='items', on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField()
    def __str__(self):
        return f"{self.quantity} x {self.product.name}"
    
