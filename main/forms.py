from django.forms import ModelForm
from .models import *

class ItemForm(ModelForm):
    class Meta:
        model = Item
        fields = [
            'item_name',
            'sales_price',
            'purchase_price'
        ]