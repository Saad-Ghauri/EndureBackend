from django.shortcuts import render

# Create your views here.
def Utilization_1(request):
    return render(request, 'u11.html', context)
def Utilization_2(request):
    return render(request, 'u2.html', )
def Utilization_3(request):
    return render(request, 'u3.html', )
def Utilization_4(request):
    return render(request, 'u4.html', )
def Utilization_5(request):
    return render(request, 'u5.html', )
def Utilization_6(request):
    return render(request, 'u6.html', )

context = {
    'headers' : [
        'Utilization', 'Type', 'Date', 'Submitted', 'Refrence', 'Summary', 'Status',
    ]
}