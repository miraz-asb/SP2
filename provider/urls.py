from django.urls import path
from . import views

urlpatterns = [

    path('ProviderOverview',views.ProviderOverview),
    path('ProviderOverview1',views.ProviderOverview1),
    path('ProviderViewRequestApprej',views.ProviderViewRequestApprej),
    path('ProviderViewRequestApprej1',views.ProviderViewRequestApprej1),
    path('ProviderViewRequestHoldAck',views.ProviderViewRequestHoldAck),
    path('ProviderViewRequestHoldAck1',views.ProviderViewRequestHoldAck1),
    path('ProviderViewRequests',views.ProviderViewRequests),
    path('ProviderViewRequestsOptions',views.ProviderViewRequestsOptions),
    path('Register1',views.Register1),
]
