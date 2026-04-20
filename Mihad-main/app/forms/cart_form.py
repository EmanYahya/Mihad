from django import forms
from ..models.cart import Cart


class CartForm(forms.ModelForm):
    quantity = forms.IntegerField(
        min_value=1,
        label='Quantity',
        widget=forms.NumberInput(attrs={'class': 'form-control'})
    )

    class Meta:
        model = Cart
        fields = ['quantity']

    def __init__(self, *args, **kwargs):
        self.product = kwargs.pop('product')
        super().__init__(*args, **kwargs)
        self.fields['quantity'].widget.attrs['max'] = 10
        self.fields['quantity'].widget.attrs['min'] = 1

    def clean_quantity(self):
        quantity = self.cleaned_data.get('quantity')
        if quantity > 10:
            raise forms.ValidationError("Only {} available".format(10))
        return quantity
