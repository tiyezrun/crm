from django.urls import path

from cashier_interface.views import Cashier_interfaceView

urlpatterns = [
    path('', Cashier_interfaceView.as_view(), name='cashier_interface'),

]