
from django.urls import path


from employee.views import EmployeeView
from shift.views import ShiftView

urlpatterns = [
    path('', ShiftView.as_view(), name='shift'),
]
