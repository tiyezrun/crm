from django.shortcuts import render
from django.views.generic import TemplateView


class ShiftView(TemplateView):
    template_name = 'shift/shift.html'

    def get(self, request, *args, **kwargs):
        context = {

        }
        return render(request, self.template_name, context)
