from .views import export_users_xls, export_styling_xls, export_report_xls
from django.urls import path

urlpatterns = [
    path('xls/', export_users_xls, name='export_users_xls'),
    path('excel-styling/', export_styling_xls, name='export_styling_excel'),
    path('report-xls/', export_report_xls, name='export_report_xls'),
]