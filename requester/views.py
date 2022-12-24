from django.shortcuts import render

# Create your views here.

def ERRORNewForm(request):
    return render(request, 'requester\ERRORNewForm.html') 

def Register(request):
    return render(request, 'requester\Register.html') 

def RequesterInitiateRequest(request):
    return render(request, 'requester\RequesterInitiateRequest.html') 

def RequesterInitiateRequest1(request):
    return render(request, 'requester\RequesterInitiateRequest1.html') 

def ReqViewRequests(request):
    return render(request, 'requester\ReqViewRequests.html')    

def ReqViewRequests1(request):
    return render(request, 'requester\ReqViewRequests1.html')                    

