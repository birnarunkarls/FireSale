from django.forms import ModelForm
from checkout.models import Checkout, Rating



class CheckoutForm(ModelForm):
    class Meta:
        model = Checkout
        exclude = ['id']






class RatingForm(ModelForm):
    class Meta:
        model = Rating
        exclude = ['id']



