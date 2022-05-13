from django.forms import ModelForm, widgets
from item.models import Bid


class NewBidForm(ModelForm):
    class Meta:
        model = Bid
        exclude = ['id', 'buyer', 'item']
        widgets = {
            'amount': widgets.TextInput(attrs={'class':'form-control'})
        }
