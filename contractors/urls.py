from django.urls import path

from contractors.views import CustomersView, SuppliersView

urlpatterns = [
    path('customers/', CustomersView.as_view(), name='customers'),
    path('suppliers/', SuppliersView.as_view(), name='suppliers'),

]
