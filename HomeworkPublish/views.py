from django.shortcuts import render,redirect
from django.http import HttpResponse
from .forms import HomeworkFrom
from django.contrib.auth.models import User
from .models import Homework 

# Create your views here.
def Homework_list(request):
    homework = Homework.objects.all()
    context = {'homework':homework}
    return render(request, 'HomeworkPublish/list.html',context)

def Homework_Publish(request,id):
    homework = Homework()
    if request.method == "POST":
        Homework_Publish_form = HomeworkFrom(data=request.POST)
        if Homework_Publish_form.is_valid():
            homework.courseNum = id
            homework.Homework_text = request.POST['Homework_text']
            homework.deadline_date = request.POST['deadline_date']
            homework.deadline_time = request.POST['deadline_time']
            homework.save()
            return HttpResponse("已发布，请返回刷新页面")
        else:
            return HttpResponse("作业内容有误，请重新填写。")
    return render(request,'HomeworkPublish/Publish.html',{'hw':homework})

def Homework_delete(request,id):
    homework = Homework.objects.get(id=id)
    context = {'homework':homework}
    homework.delete()
    return HttpResponse("已删除，请返回刷新页面")