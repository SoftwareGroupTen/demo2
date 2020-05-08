from django.shortcuts import render,render_to_response
from django.http import HttpResponse
from .models import userfile

def register(request):
    uf=userfile()
    if request.method == "POST":
        uf.username = request.POST['name']
        uf.username = request.POSt['courseNum']
        uf.headImg = request.FILES.get('tttt',None)

        uf.save()
        return HttpResponse('upload ok!')
    return render(request,'upload/register.html',{'uf':uf})

def display(request):
    filelist = userfile.objects.all()
    context = {'filelist':filelist}
    return render(request,"upload/filelist.html",context)