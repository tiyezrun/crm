
from django.urls import path

from directory.views import DirectoryView, GoodsView, ServiceView

urlpatterns = [
    path('', DirectoryView.as_view(), name='directory'),
    path('goods/', GoodsView.as_view(), name='goods'),
    path('service/', ServiceView.as_view(), name='service'),

]
