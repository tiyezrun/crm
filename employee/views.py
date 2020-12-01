from django.shortcuts import render
from django.views.generic import TemplateView


class EmployeeView(TemplateView):
    template_name = 'employee/employee.html'

    def get(self, request, *args, **kwargs):
        context = {

        }
        return render(request, self.template_name, context)
