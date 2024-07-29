from django.forms import ModelForm
from.models import Order


class BikePurchaseForm(ModelForm):
    class Meta:
        model = Order
        fields = ['name', 'surname', 'phone_number']