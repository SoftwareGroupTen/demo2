from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.forms import UserCreationForm,UserChangeForm, PasswordChangeForm
from django.http import HttpResponse
from django.db.models import Q
from .forms import 自定义注册表单,自定义编辑表单,自定义登录表单
from .models import 普通会员表
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from HomeworkPublish.models import Homework
from upload.models import userfile
from .models import course
from .models import stucourse
from .models import asscourse

def 主页(request):
    if request.user.is_authenticated:
        mycourse=course.objects.filter(teacherName = request.user.username)
        sc = stucourse.objects.filter(studentName = request.user.username)
        ac = asscourse.objects.filter(assistantName = request.user.username)
        hw=Homework.objects.all()
        uf=userfile.objects.all()
        us=普通会员表.objects.all()
        nowu=request.user
        request.session['role']=nowu.普通会员表.身份
        context={'hw':hw,'uf':uf,'us':us,'mycourse':mycourse,'sc':sc,'ac':ac}
        return render(request, 'Login/home.html',context)
    else:
        return render(request,'Login/home.html')



def 登录(require):
    if require.method == 'POST':
        登录表单 = 自定义登录表单(data= require.POST)
        if 登录表单.is_valid():

            用户 = authenticate(require,username=登录表单.cleaned_data['username'] ,password=登录表单.cleaned_data['password'] )

            login(require,用户)
            return redirect('Login:主页')
    else:
        登录表单 = 自定义登录表单()

    内容 = {'登录表单':登录表单, '用户':require.user}
    return render(require, 'Login/login.html',内容)


def 登出(request):
    try:
        del request.session['role']
    except KeyError:
        pass
    logout(request)
    return redirect('Login:主页')


def 注册(require):
    if require.method == 'POST':
        注册表单 = 自定义注册表单(require.POST)
        if 注册表单.is_valid():
            注册表单.save()
            用户 = authenticate(username=注册表单.cleaned_data['username'] ,password=注册表单.cleaned_data['password1'] )
            用户.email = 注册表单.cleaned_data['email']
            普通会员表(用户=用户,昵称=注册表单.cleaned_data['昵称'],身份=注册表单.cleaned_data['身份']).save()
            login(require,用户)
            return redirect('Login:主页')
    else:
        注册表单 = 自定义注册表单()

    内容 = {'注册表单':注册表单}
    return render(require, 'Login/register.html', 内容)

@login_required(login_url='Login:登录')
def 个人中心(require):
    内容 = {'用户': require.user}
    return render(require, 'Login/user-center.html', 内容)

@login_required(login_url='Login:登录')
def 编辑个人信息(require):
    if require.method == 'POST':
        编辑表单 = 自定义编辑表单(require.POST,instance = require.user)
        if 编辑表单.is_valid():
            编辑表单.save()
            require.user.普通会员表.昵称 = 编辑表单.cleaned_data['昵称']
            require.user.普通会员表.身份 = 编辑表单.cleaned_data['身份']
            require.user.普通会员表.save()
            return redirect('Login:个人中心')
    else:
        编辑表单 = 自定义编辑表单(instance = require.user)

    内容 = {'编辑表单':编辑表单, '用户':require.user}
    return render(require, 'Login/edit-profile.html', 内容)



@login_required(login_url='Login:登录')
def 修改密码(require):
    if require.method == 'POST':
        改密表单 = PasswordChangeForm(data= require.POST,user = require.user)
        if 改密表单.is_valid():
            改密表单.save()
            return redirect('Login:登录')
    else:
        改密表单 = PasswordChangeForm(user = require.user)

    内容 = {'改密表单':改密表单, '用户':require.user}
    return render(require, 'Login/change-password.html', 内容)


def upload(request,id):
    uf=userfile()
    if request.method == "POST":
        uf.username = request.user.username
        uf.homework = Homework.objects.get(id=id)
        uf.headImg = request.FILES.get('tttt',None)
        uf.save()
        return HttpResponse('upload ok!')
    return render(request,'Login/upload.html',{'uf':uf})

def addcourse(request):
    Nowcourse = course()
    if request.method == "POST":
        Nowcourse.teacherName = request.user.username
        Nowcourse.courseNum = request.POST['courseNum']
        Nowcourse.courseName = request.POST['courseName']
        Nowcourse.save()
        return HttpResponse('添加成功')
    return render(request,'Login/addcourse.html',{'Nowcourse':Nowcourse})

def joincourse(request):
    search = request.GET.get('search')
    if search:
        target = course.objects.filter(
            Q(courseNum__icontains=search)
        )
    else:
        search=''
        target =  course.objects.all()
    join = request.GET.get('join')
    if join:
        joinCourse = stucourse()
        joinCourse.studentName = request.user.username
        courseID = request.GET.get('ID')
        joinCourse.thecourse = course.objects.get(id=courseID)
        joinCourse.save()
    context = {'search':search,'target':target}
    return render(request,"Login/joincourse.html",context)


def coursedetail(request,id):
    mycourse=course.objects.get(id = id)
    sc = stucourse.objects.filter( thecourse_id = id)
    hw=Homework.objects.filter(courseNum = id)
    context = {'mycourse':mycourse,'sc':sc,'hw':hw}
    return render(request,'Login/coursedetail.html',context)

def coursedelete(request,id):
    target = course.objects.get(id=id)
    target.delete()
    return HttpResponse("已删除课程")

def addassistant(request,id):
    assistant = asscourse()
    Course = course.objects.get(id=id)
    if request.method == "POST":
        assistant.assistantName = request.POST['assistantName']
        assistant.thecourse = Course
        assistant.save()
        return HttpResponse('添加成功')
    return render(request,'Login/addassistant.html',{'Course':Course})

def homeworkdetail(request,id):
    homework = Homework.objects.get(id=id)
    time = timezone.now()
    context = {'homework':homework,'time':time}
    return render(request,'Login/homeworkdetail.html',context)

def makecomments(request):
    hwID = request.GET.get('hwID')
    course = Homework.objects.get(id=hwID)
    studentlist = stucourse.objects.filter(thecourse_id=course.courseNum)
    if hwID:
        homeworklist = userfile.objects.filter(homework_id=hwID)
        uncomplete = []
        for name1 in studentlist:
            for name2 in homeworklist:
                if name1.studentName == name2.username:
                    pass
                else:
                    uncomplete.append(name1)
        
        context = {'homeworklist':homeworklist,'uncomplete':uncomplete}
    else:
        context = {}
    return render(request,'Login/makecomment.html',context)