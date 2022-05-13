from django.forms import ModelForm, widgets
from checkout.models import Checkout, Rating




class CheckoutForm(ModelForm):
    class Meta:
        model = Checkout
        exclude = ['id', 'user', 'item' ]
        widgets = {
            'full_name': widgets.TextInput(attrs={'class':'form-control'}),
            'street_name': widgets.TextInput(attrs={'class':'form-control'}),
            'house_number': widgets.TextInput(attrs={'class':'form-control'}),
            'postal_code': widgets.TextInput(attrs={'class':'form-control'}),
            'city': widgets.TextInput(attrs={'class':'form-control'}),
            'country': widgets.Select(attrs={'class':'form-control'}),
            'cardholder_name': widgets.TextInput(attrs={'class':'form-control'}),
            'cardnumber': widgets.TextInput(attrs={'class':'form-control'}),
            'expiration_date': widgets.TextInput(attrs={'class':'form-control'}),
            'cvc': widgets.TextInput(attrs={'class':'form-control'}),
        }



class RatingForm(ModelForm):
    class Meta:
        model = Rating
        exclude = ['id', 'seller']
        widgets = {
            'rating': widgets.TextInput(attrs={'class':'form-control'})
        }



