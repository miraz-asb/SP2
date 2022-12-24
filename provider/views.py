from django.shortcuts import render

# Create your views here.
def ProviderOverview(request):
    return render(request, 'provider\ProviderOverview.html') 

def ProviderOverview1(request):
    return render(request, 'provider\ProviderOverview1.html')   

def ProviderViewRequestApprej(request):
    return render(request, 'provider\ProviderViewRequestApprej.html')       

def ProviderViewRequestApprej1(request):
    return render(request, 'provider\ProviderViewRequestApprej1.html') 

def ProviderViewRequestHoldAck(request):
    return render(request, 'provider\ProviderViewRequestHoldAck.html')   

def ProviderViewRequestHoldAck1(request):
    return render(request, 'provider\ProviderViewRequestHoldAck1.html')       

def ProviderViewRequests(request):
    return render(request, 'provider\ProviderViewRequests.html') 

def ProviderViewRequestsOptions(request):
    return render(request, 'provider\ProviderViewRequestsOptions.html')   

def Register1(request):
    return render(request, 'provider\Register1.html')    