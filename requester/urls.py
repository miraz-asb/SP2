from django.urls import path
from . import views

urlpatterns = [

    path('ERRORNewForm',views.ERRORNewForm,name='ERRORNewForm_screan'),
    path('Register',views.Register),
    path('RequesterInitiateRequest',views.RequesterInitiateRequest),
    path('RequesterInitiateRequest1',views.RequesterInitiateRequest1),
    path('ReqViewRequests',views.ReqViewRequests),
    path('ReqViewRequests1',views.ReqViewRequests1),
    
]

