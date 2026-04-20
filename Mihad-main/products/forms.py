from django import forms
from .models import *

class ProductForm(forms.ModelForm):

    name = forms.CharField(
        label='Product Name',
        max_length=200,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter product name'}),
    )
    description = forms.CharField(
        label='Description',
        widget=forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Enter description'}),
    )
    price = forms.DecimalField(
        label='Price',
        decimal_places=2,
        max_digits=10,
        widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Enter price'}),
    )
    available_sizes = forms.ModelMultipleChoiceField(
        label='Available Sizes',
        queryset=Size.objects.all(),
        widget=forms.CheckboxSelectMultiple(attrs={'class': 'form-check-input'}),
    )
    available_colors = forms.ModelMultipleChoiceField(
        label='Available Colors',
        queryset=Color.objects.all(),
        widget=forms.CheckboxSelectMultiple(attrs={'class': 'form-check-input'}),
    )
    category = forms.ModelChoiceField(
        label='Category',
        queryset=Category.objects.all(),
        widget=forms.Select(attrs={'class': 'form-select'}),
    )
    #brand = forms.ModelChoiceField(
      #  label='Brand',
      #   queryset=Brand.objects.all(),
      #  widget=forms.Select(attrs={'class': 'form-select'}),
  # )
    image = forms.ImageField(
        label='Product Image',
        widget=forms.ClearableFileInput(attrs={'class': 'form-control'}),
        required=False,
    )
    is_newarrival = forms.BooleanField(
        label='New Arrival',
        required=False,
        widget=forms.CheckboxInput(attrs={'class': 'form-check-input'}),
    )
    class Meta:
        model = Product
        fields = ['name', 'description', 'price', 'available_sizes', 'available_colors', 'category', 'image', 'is_newarrival']

    def clean_price(self):
        price = self.cleaned_data['price']
        if price <= 0:
            raise forms.ValidationError("Price must be greater than zero.")
        return price

    def clean_image(self):
        image = self.cleaned_data['image']
        if image and image.size > 5 * 1024 * 1024: # Max file size is 5MB
            raise forms.ValidationError("Image size must be less than 5MB.")
        return image

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['name'].widget.attrs['class'] = 'form-control'
        self.fields['description'].widget.attrs['class'] = 'form-control'
        self.fields['price'].widget.attrs['class'] = 'form-control'
        self.fields['available_sizes'].widget.attrs['class'] = 'form-control'
        self.fields['available_colors'].widget.attrs['class'] = 'form-control'
        self.fields['category'].widget.attrs['class'] = 'form-control'
    #    self.fields['brand'].widget.attrs['class'] = 'form-control'
        self.fields['image'].widget.attrs['class'] = 'form-control-file'
        self.fields['is_newarrival'].widget.attrs['class'] = 'form-check-input'


   # def __init__(self, *args, **kwargs):
   #     super().__init__(*args, **kwargs)
   #     self.fields['available_sizes'].widget.attrs.update({'class': 'form-check-input'})
   #     self.fields['available_colors'].widget.attrs.update({'class': 'form-check-input'})
#class ProductForm(forms.ModelForm):
#    class Meta:
#        model = Product
#        fields = ['name', 'description', 'price', 'category', 'image']
#        widgets = {
#            'name': forms.TextInput(attrs={'class': 'form-control'}),
#            'description': forms.Textarea(attrs={'class': 'form-control'}),
#            'price': forms.NumberInput(attrs={'class': 'form-control'}),
#            'category': forms.Select(attrs={'class': 'form-control'}),
#            'image': forms.ClearableFileInput(attrs={'class': 'form-control-file'})
#        }


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name']
        labels = {
            'name': 'Category Name',
        }


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ('rating', 'comment')
        widgets = {
           # 'rating': forms.Select(choices=Review.RATING_CHOICES),
            'comment': forms.Textarea(attrs={'rows': 5}),
        }

    def clean_rating(self):
        rating = self.cleaned_data['rating']
        if rating < 1 or rating > 5:
            raise forms.ValidationError('Rating must be between 1 and 5')
        return rating

