from django.urls import path 
from . import views


urlpatterns = [
    path('', views.checkout),
    path('success', views.success, name='success'),
    path('cancel', views.cancel, name='cancel'),
    path('create-checkout-session', views.create_checkout_session, name='create-checkout-session')
]