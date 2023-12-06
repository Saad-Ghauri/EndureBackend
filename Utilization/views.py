from django.shortcuts import render

# Create your views here.
def Utilization_1(request):
    return render(request, 'u11.html', context)
def Utilization_2(request):
    return render(request, 'u2.html', u2context)
def Utilization_3(request):
    return render(request, 'u3.html', u3headers)
def Utilization_4(request):
    return render(request, 'u4.html', u4headers)
def Utilization_5(request):
    return render(request, 'u5.html', u5headers)
def Utilization_6(request):
    return render(request, 'u6.html', u6headers)

context = {
    'headers' : [
        'Utilization', 'Type', 'Date', 'Submitted', 'Refrence', 'Summary', 'Status',
    ]
}
u2context = {
    'headers' : [
        'Product', 'Mfg#', 'Notes', 'Quantity', 'Cost', 'Availability', 'Substitutes',
    ]
}


u3headers = {
    'headers': [ 'Utilization', 'Date', 'Case', 'Refrence', 'Submitted', 'Items', 'Status']   
  }


u4headers = {
    'headers': [ 'Utilization', 'Date', 'Type', 'Submitted', 'Reference', 'Summary', 'Status']   
  }
u5headers = {
    'headers': [ 'Utilization', 'Date', 'Reference', 'Submitted', 'Case Summary', 'Items', 'Status']   
  }
u6headers = {
    'headers': [ 'Utilization', 'Date', 'Reference', 'Submitted', 'Case Summary', 'Items', 'Status']   
  }
