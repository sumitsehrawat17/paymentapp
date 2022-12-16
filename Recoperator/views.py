from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response

from .models import rechargeplans,toperator
from .serializer import Planserializers
# using rest framework classes

def operators(request):
    op = toperator.objects.all()
    return render(request,'operators.html',{'operator':op})






class rechargeData(APIView):
    def get(self,request):
        data = rechargeplans.objects.all()
        serliazer = Planserializers(data,many = True)
        return Response(serliazer.data)


class plans(APIView):
    authentication_classes = []
    permission_classes = []
    def get(self,request,name):
       
        data = rechargeplans.objects.filter(op = name)
        serliazer = Planserializers(data,many = True)
       



        return Response(serliazer.data)




def getoperator(request,name):
    return render(request,'opplans.html',{'name':name})
