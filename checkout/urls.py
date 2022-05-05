from django.urls import path

from . import views

urlpatterns = [

    # checkout
    path('checkout_phase1', views.checkout_phase1),
    path('checkout_phase2', views.checkout_phase2),
    path('checkout_phase3', views.checkout_phase3),

]