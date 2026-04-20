from django import forms
from django_countries.fields import CountryField

from .widgets import CustomClearableFileInput
from ..models import Address


class AddressForm(forms.ModelForm):
    """Form for creating or updating an address."""

    class Meta:
        model = Address
        fields = [
            'street_address',
            'apartment_address',
            'country',
            'zip',
            'address_type',
        ]

    # Add widget to apartment_address field
    apartment_address = forms.CharField(required=False, widget=forms.TextInput(attrs={'placeholder': 'Apartment or suite'}))

    # Add CountryField to country field
    country = CountryField(blank_label='(select country)').formfield()

    # Add CSS class to each form field
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'form-control'

    # Override clean method to ensure a valid zip code is entered for the selected country
    def clean_zip(self):
        country = self.cleaned_data.get('country')
        zip_code = self.cleaned_data.get('zip')
        if country and zip_code:
            if country.alpha_2 == 'US':
                valid_zip = forms.fields.RegexField(regex=r'^\d{5}(-\d{4})?$')
            else:
                valid_zip = forms.fields.RegexField(regex=r'^[a-zA-Z0-9 -]+$')
            try:
                valid_zip.clean(zip_code)
            except forms.ValidationError:
                raise forms.ValidationError("Please enter a valid zip code for the selected country.")
        return zip_code
