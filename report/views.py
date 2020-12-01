from django.shortcuts import render
from django.views.generic import TemplateView


class ReportView(TemplateView):
    template_name = 'report/report.html'

    def get(self, request, *args, **kwargs):
        context = {

        }
        return render(request, self.template_name, context)
