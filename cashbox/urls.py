
from django.urls import path

from cashbox.views import CashboxView


urlpatterns = [
    path('', CashboxView.as_view(), name='cashbox'),
]
