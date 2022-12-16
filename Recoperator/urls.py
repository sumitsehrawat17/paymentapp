from django.urls import path
from .views import *

urlpatterns = [
path('',operators,name = "operator"),
path('getplans',rechargeData.as_view(),name = "rechargedata"),
path('plans/<str:name>',plans.as_view(),name = "operatorplans"),
path('getoperator/<str:name>',getoperator,name="getoperator"),
]