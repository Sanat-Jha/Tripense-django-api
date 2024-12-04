from django.contrib import admin
from django.urls import path,include
from .views import *

urlpatterns = [
   path('newtrip/',newtrip,name='newtrip'),
   path('home/',home,name='home'),
   path('trip/',trip,name='trip'),
   path('newmember/',newmember,name='newmember'),
   path('newpayment/',newpayment,name='newpayment'),
   path('removemember/',removemember,name='removemember'),
   path('removepayment/',removepayment,name='removepayment'),
   path('toggledue/',toggledue,name='toggledue'),
   path('deletetrip/',deletetrip,name='deletetrip'),
]
