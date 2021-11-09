from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models    import Product, SalesInvoice, SalesInvoiceDetails 

from .forms import ProductForm, SalesInvoiceDetailsForm
from .forms import SalesInvoiceForm


# Create your views here.

def product_list(request):
    context = {'product_list': Product.objects.all()}
    return render(request, "product_list.html",context)

def product_form(request, id=0):
        if request.method == "GET":
            if id == 0:
                form = ProductForm()
            else:
                product = Product.objects.get(pk=id)
                form = ProductForm(instance=product)
            return render(request, "product_form.html", {'form': form})
        else:
            if id == 0:
                form = ProductForm(request.POST)
            else:
                product = Product.objects.get(pk=id)
                form = ProductForm(request.POST,instance=product)
            if form.is_valid():
                form.save()
            return redirect('/storemanagement/list')

def sales_invoice_details_form(request, id=0):
    if request.method == "GET":
        if id == 0:
            form = SalesInvoiceDetailsForm()
        else:
            salesInvoiceDetails = SalesInvoiceDetails.objects.get(pk=id)
            form = SalesInvoiceDetailsForm(instance=salesInvoiceDetails)
        return render(request, "sales_invoice_details_form.html", {'form': form})
    else:
        if id == 0:
            form = SalesInvoiceDetailsForm(request.POST)
        else:
            salesInvoiceDetails = SalesInvoiceDetails.objects.get(pk=id)
            form = SalesInvoiceDetailsForm(request.POST,instance=salesInvoiceDetails)
        if form.is_valid():
            form.save()
        return redirect('/storemanagement/salesInvoiceDetailsList')

def sales_invoice_form(request):
        if request.method == "GET":
            form = SalesInvoiceForm()
            return render(request,'sales_invoice_form.html',{'form': form})
        else:
            form = SalesInvoiceForm(request.POST)
            if form.is_valid():
                form.save()
            return redirect('/storemanagement/salesInvoiceDetails')

def sales_invoice_details_list(request):
    context = {'sales_invoice_details_list': SalesInvoiceDetails.objects.all()}
    return render(request, "sales_invoice_details_list.html",context)

def sales_invoice_list(request):
    context = {'sales_invoice_list': SalesInvoice.objects.all()}
    return render(request, "sales_invoice_list.html",context)

