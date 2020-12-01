from django.shortcuts import render
from django.views.generic import TemplateView


class CashboxView(TemplateView):
    template_name = 'cashbox/cashbox.html'

    def get(self, request, *args, **kwargs):
        context = {

        }
        return render(request, self.template_name, context)
