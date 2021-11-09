from django.urls import path
from . import views

urlpatterns = [
    path('', views.product_form,name='product_insert'),
    path('<int:id>', views.product_form,name='product_update'),
    path('list', views.product_list,name='product_list'),
    path('salesInvoice', views.sales_invoice_form,name='sales_invoice'),
    path('salesInvoiceList', views.sales_invoice_list,name='sales_invoice_list'),
    path('salesInvoiceDetails', views.sales_invoice_details_form,name='sales_invoice_details'),
    path('salesInvoiceDetailsList/<int:id>', views.sales_invoice_details_form,name='invoice_details_update'),
    path('salesInvoiceDetailsList', views.sales_invoice_details_list,name='sales_invoice_details_list')
]