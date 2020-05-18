from django.shortcuts import render,redirect
from django.http import HttpResponse
from .forms import HomeworkFrom
from django.contrib.auth.models import User
from .models import Homework 
from notifications.signals import notify
from Login.models import stucourse
from Login.models import course
from django.contrib import messages
# Create your views here.

#展示作业列表
def Homework_list(request):
    homework = Homework.objects.all()
    context = {'homework':homework}
    return render(request, 'HomeworkPublish/list.html',context)

#作业发布
def Homework_Publish(request,id):
    homework = Homework()
    if request.method == "POST":
        Homework_Publish_form = HomeworkFrom(data=request.POST)
        if Homework_Publish_form.is_valid():
            homework.courseNum = id
            homework.Homework_title = request.POST['Homework_title']
            homework.Homework_text = request.POST['Homework_text']
            homework.deadline_date = request.POST['deadline_date']
            homework.deadline_time = request.POST['deadline_time']
            students = stucourse.objects.filter(thecourse_id = id)
            c = course.objects.get(id=id)
            homework.save()
            for student in students:
                stu = User.objects.get(username = student.studentName)
                notify.send(
                    request.user,
                    recipient=stu,
                    verb='创建了作业',
                    target=c,
                    action_object=homework,
                    
                ) 
            messages.info(request,"发布成功")
            #return HttpResponse("已发布，请返回刷新页面")
        else:
            messages.error(request,"作业内容有误，请重新填写")
            #return HttpResponse("作业内容有误，请重新填写。")
    return render(request,'HomeworkPublish/Publish.html',{'hw':homework})

#作业删除
def Homework_delete(request,id):
    homework = Homework.objects.get(id=id)
    ID=homework.courseNum
    homework.delete()
    mycourse = course.objects.get(id=ID)
    sc = stucourse.objects.filter( thecourse_id = ID)
    hw=Homework.objects.filter(courseNum = ID)
    context = {'mycourse':mycourse,'sc':sc,'hw':hw}
    messages.info(request,"已删除此作业")
    return render(request,'Login/coursedetail.html',context)