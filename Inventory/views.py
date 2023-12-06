from django.shortcuts import render
from django.http import HttpResponse

from Inventory.models import Vendor

# Create your views here.


def Characteristics_View(request):
    return render(request,'char.html', )

def Inventory_View(request):
    return render(request,'inventory.html', context)


def Accounting_View(request):
    return render(request,'accounting.html')

def Purchasing_View(request):
    return render(request,'pur.html', Purchasing_table)

def Vendors_View(request):
   vendors = Vendor.objects.all()
   headers = ["Vendor", "Vendor#", "Price", "Additional Terms", "Representatives", "Status"]
   context = {
        'vendors': vendors,
        'headers': headers,
    }
   return render(request,'vendors.html', context)



context = {
    'fruits': [ 'Vendors', 'Exp Date', 'Lot#', 'Notes', 'Usage', 'Available', 'Reserved' , 'On Hold', 'Total' ],   
  }



Purchasing_table = {
    'headers' : ['PO', "Vendor", 'Date', 'Fulfullment', 'Items', 'Requested', 'Purchased', 'Alerts']
}


def index(request):
    return render(request,'characteristics.html')