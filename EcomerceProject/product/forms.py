from django import forms
from .models import Product
class productForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(productForm,self).__init__(*args, **kwargs)
        self.fields['category'].empty_label = "Select"
        self.fields['brand'].empty_label = "Select"
        self.fields['slug'].required = False
        self.fields['category'].required = False
        self.fields['image'].required = False
        self.fields['status'].required = False

