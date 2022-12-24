from django.shortcuts import render

# Create your views here.
def admin(request):
    return render(request, 'admin\Admin.html') 

def admin1(request):
    return render(request, 'admin\Admin1.html')   

def login(request):
    return render(request, 'admin\login.html')       

