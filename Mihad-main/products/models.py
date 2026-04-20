from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
# from app.models.user import User
from slugify import slugify

class Category(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    image = models.ImageField(upload_to='categories/', blank=True)

    class Meta:
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('category_detail', args=[self.slug])


class SubCategory(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    category = models.ForeignKey(Category, related_name='subcategories', on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = 'Subcategories'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('subcategory_detail', args=[self.category.slug, self.slug])


class Size(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class Color(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=20)
    code = models.CharField(max_length=6)

    def __str__(self):
        return self.name

#class Brand(models.Model):
  #  id = models.BigAutoField(primary_key=True)
  # name = models.CharField(max_length=200)
  # logo = models.ImageField(upload_to='products/', blank=True)


class Product(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=200)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    available_sizes = models.ManyToManyField(Size)
    available_colors = models.ManyToManyField(Color)
    category = models.ForeignKey(Category, on_delete=models.PROTECT)
    # brand = models.ForeignKey(Brand, on_delete=models.PROTECT)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    seller = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='products/', blank=True)
    is_featured = models.BooleanField(default=False)
    is_newarrival = models.BooleanField(default=False)
    slug = models.SlugField(unique=True)

    class Meta:
        ordering = ['-created_at']

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super(Product, self).save(*args, **kwargs)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('app:product_detail', args=[self.subcategory.category.slug, self.subcategory.slug, self.slug])


#class ProductVariant(models.Model):
#    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='variants')
#    size = models.ForeignKey(Size, on_delete=models.CASCADE)
#    color = models.ForeignKey(Color, on_delete=models.CASCADE)
#    image = models.ImageField(upload_to='product_variants/', blank=True)
#    price = models.DecimalField(max_digits=10, decimal_places=2)
#
#    def __str__(self):
#        return f'{self.product.name} ({self.size.name}, {self.color.name})'


class Tag(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=50)
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.name


class ProductTag(models.Model):
    id = models.BigAutoField(primary_key=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE)

    def __str__(self):
        return f'Tag "{self.tag.name}" on "{self.product.name}"'


class Review(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    rating = models.PositiveIntegerField()
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'Review for {self.product.name}'

