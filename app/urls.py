from django.urls import path
from . import views

urlpatterns=[
    path('',views.index,name='home'),
    path('1',views.create,name='create'),
    path('2',views.pin_gen,name='pin'),
    path('3',views.valid_otp,name='otp'),
    path('4',views.balance,name='balance'),
    path('5',views.withdrawl,name='take'),
    path('6',views.Deposit,name='deposite'),
    path('7',views.transefer,name='transfer')
]