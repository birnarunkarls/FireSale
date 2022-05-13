from django.urls import path

from . import views

urlpatterns = [

    # checkout
    path('checkout_phase1/<int:id>', views.checkout_phase1, name="checkout-checkout_phase1"),
    path('checkout_phase2/<int:id>', views.checkout_phase2, name="checkout-checkout_phase2"),
    path('rating/<int:id>', views.rating, name="checkout-rating")

]