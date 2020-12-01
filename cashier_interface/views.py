from django.shortcuts import render
from django.views.generic import TemplateView

class Cashier_interfaceView(TemplateView):
    template_name = 'cashier_interface/cashier_interface.html'

    def get(self, request, *args, **kwargs):
        context = {

        }
        return render(request, self.template_name, context)