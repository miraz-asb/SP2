from django.urls import path
from . import views

urlpatterns = [

    path('admin',views.admin,name='admin_screan'),
    path('admin1',views.admin1,name='admin1_screan'),
    path('login',views.login,name='login_screan'),
    

]