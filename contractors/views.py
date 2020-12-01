from django.shortcuts import render
from django.views.generic import TemplateView


class ContractorsView(TemplateView):
    template_name = 'contractors/customers.html'

    def get(self, request, *args, **kwargs):
        context = {

        }
        return render(request, self.template_name, context)


class CustomersView(TemplateView):
    template_name = 'contractors/customers.html'

    def get(self, request, *args, **kwargs):
        context = {

        }
        return render(request, self.template_name, context)


class SuppliersView(TemplateView):
    template_name = 'contractors/suppliers.html'

    def get(self, request, *args, **kwargs):
        context = {

        }
        return render(request, self.template_name, context)
