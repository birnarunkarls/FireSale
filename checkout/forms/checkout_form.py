from django.forms import ModelForm
from checkout.models import Payment


class CheckoutPaymentForm(ModelForm):
    class Meta:
        model = Payment




