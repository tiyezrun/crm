
from django.urls import path


from employee.views import EmployeeView

urlpatterns = [
    path('', EmployeeView.as_view(), name='employee'),
]
