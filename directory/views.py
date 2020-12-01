from django.shortcuts import render
from django.views.generic import TemplateView


class DirectoryView(TemplateView):
    template_name = 'directory/goods.html'

    def get(self, request, *args, **kwargs):
        context = {

        }
        return render(request, self.template_name, context)


class GoodsView(TemplateView):
    template_name = 'directory/goods.html'

    def get(self, request, *args, **kwargs):
        context = {

        }
        return render(request, self.template_name, context)


class ServiceView(TemplateView):
    template_name = 'directory/goods.html'

    def get(self, request, *args, **kwargs):
        context = {

        }
        return render(request, self.template_name, context)
