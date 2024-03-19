from django import forms

from src.accounts.models import Address
from src.shopping.models import Order


class OrderForm(forms.ModelForm):

    class Meta:
        model = Order
        fields = ['address']
        widgets = {'address': forms.Select()}

    def __init__(self, *args, **kwargs):
        pk = kwargs.pop('user_id')
        super().__init__(*args, **kwargs)

        self.fields['address'].queryset = Address.objects.filter(user_id=pk)
