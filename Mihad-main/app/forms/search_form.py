from django import forms


class SearchForm(forms.Form):
    query = forms.CharField(label='Search Products')

    def __init__(self, *args, **kwargs):
        super(SearchForm, self).__init__(*args, **kwargs)
        self.fields['query'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Enter search keyword'})

    def clean(self):
        cleaned_data = super(SearchForm, self).clean()
        query = cleaned_data.get('query')

        if not query:
            raise forms.ValidationError("Please enter a search query.")

        return cleaned_data
