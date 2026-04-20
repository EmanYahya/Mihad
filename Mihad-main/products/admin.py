from django.contrib import admin
from .models import Category, SubCategory, Product, Size, Color
from app.models.user import UserProfile, Notification
from app.models.cart import Order, OrderItem


# Register your models here.
admin.site.register(Category)
admin.site.register(SubCategory)
admin.site.register(Product)
admin.site.register(Size)
admin.site.register(Color)
admin.site.register(UserProfile)
admin.site.register(Notification)
class OrderItemInline(admin.TabularInline):
    model = OrderItem
    extra = 0
    can_delete = False
    readonly_fields = ('product', 'price', 'quantity')

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    # المعلومات اللي هتظهر في الجدول بره
    list_display = ['id', 'user', 'total_price', 'status', 'created_at']
    # الفلاتر اللي في الجنب
    list_filter = ['status', 'created_at']
    # ربط المنتجات بالطلب في نفس الصفحة
    inlines = [OrderItemInline]
