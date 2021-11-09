from django import forms
from .models import Product, SalesInvoiceDetails,SalesInvoice


class ProductForm(forms.ModelForm):

    class Meta:
        model = Product
        fields = ('productCode','productName','sellingPrice')
        labels = {
            'productCode':'Product Code',
            'productName':'Product Name',
            'sellingPrice': 'selling Price'
            
        }
   
    def __init__(self, *args, **kwargs):
        super(ProductForm,self).__init__(*args, **kwargs)
        

class SalesInvoiceForm(forms.ModelForm):
    class Meta:
        model = SalesInvoice
        fields = ('__all__')
        labels = {
            'invoiceNumber':'Invoice Number',
            'invoiceDate':'Invoice Date',
            'customerName': 'Customer Name',
            'totalAmout' : 'Total Amount'
        }

    def __init__(self, *args, **kwargs):
        super(SalesInvoiceForm,self).__init__(*args, **kwargs)
        self.fields['invoiceNumber'].empty_label = "Select"

class SalesInvoiceDetailsForm(forms.ModelForm):
    class Meta:
        model = SalesInvoiceDetails
        fields = ('__all__')
        labels = {
            'saleInovoiceId':'Sale Invoice ID',
            'lineNumber':'Line Number',
            'productId': 'Product ID',
            'productName' : 'Product Name',
            'quantity'     : 'Quantity',
            'unitPrice'     : 'Unit Price',
            'amount'           : 'Amount'
        }
    
    def __init__(self, *args, **kwargs):
        super(SalesInvoiceDetailsForm,self).__init__(*args, **kwargs)
        self.fields['saleInvoiceId'].empty_label = "Select"
       
       
       