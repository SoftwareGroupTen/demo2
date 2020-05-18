from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.forms import UserCreationForm,UserChangeForm, PasswordChangeForm
from django.http import HttpResponse
from django.db.models import Q
from django.contrib.auth.models import User
from notifications.signals import notify
from django.contrib import messages
from .forms import customizedregisterForm,customizededitForm,customizedloginForm
from .models import normaluserform
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from HomeworkPublish.models import Homework
from upload.models import userfile
from comment.models import Comment
from .models import course
from .models import stucourse
from .models import asscourse
import markdown

#主页，包含登录模块，以及传各种参数
def PAGE(request):
    if request.user.is_authenticated:
        mycourse=course.objects.filter(teacherName = request.user.username)
        sc = stucourse.objects.filter(studentName = request.user.username)
        ac = asscourse.objects.filter(assistantName = request.user.username)
        hw=Homework.objects.all()
        uf=userfile.objects.all()
        us=normaluserform.objects.all()
        nowu=request.user
        request.session['role']=nowu.normaluserform.Identity
        context={'hw':hw,'uf':uf,'us':us,'mycourse':mycourse,'sc':sc,'ac':ac}
        return render(request, 'Login/home.html',context)
    else:
        if request.method == 'POST':
            loginform = customizedloginForm(data= request.POST)
            if loginform.is_valid():

                USER = authenticate(request,username=loginform.cleaned_data['username'] ,password=loginform.cleaned_data['password'] )

                login(request,USER)
                return redirect('Login:PAGE')
        else:
            loginform = customizedloginForm()

    Content = {'loginform':loginform, 'USER':request.user}
    return render(request, 'Login/home.html',Content)





#登出模块
def logOut(request):
    try:
        del request.session['role']
    except KeyError:
        pass
    logout(request)
    return redirect('Login:PAGE')

#注册
def Register(require):
    if require.method == 'POST':
        registerform = customizedregisterForm(require.POST)
        if registerform.is_valid():
            registerform.save()
            USER = authenticate(username=registerform.cleaned_data['username'] ,password=registerform.cleaned_data['password1'] )
            USER.email = registerform.cleaned_data['email']
            normaluserform(USER=USER,nickname=registerform.cleaned_data['nickname'],Identity=registerform.cleaned_data['Identity']).save()
            login(require,USER)
            return redirect('Login:PAGE')
    else:
        registerform = customizedregisterForm()

    Content = {'registerform':registerform}
    return render(require, 'Login/register.html', Content)

#用户中心（需登录）
@login_required(login_url='Login:logIn')
def usercenter(require):
    Content = {'USER': require.user}
    return render(require, 'Login/user-center.html', Content)
#编辑个人信息（需登录）
@login_required(login_url='Login:logIn')
def editprofile(require):
    if require.method == 'POST':
        editprofileform = customizededitForm(require.POST,instance = require.user)
        if editprofileform.is_valid():
            editprofileform.save()
            require.user.normaluserform.nickname = editprofileform.cleaned_data['nickname']
            require.user.normaluserform.Identity = editprofileform.cleaned_data['Identity']
            require.user.normaluserform.save()
            return redirect('Login:usercenter')
    else:
        editprofileform = customizededitForm(instance = require.user)

    Content = {'editprofileform':editprofileform, 'USER':require.user}
    return render(require, 'Login/edit-profile.html', Content)


#修改密码（需登录）
@login_required(login_url='Login:logIn')
def changepassword(require):
    if require.method == 'POST':
        changepasswordForm = PasswordChangeForm(data= require.POST,user = require.user)
        if changepasswordForm.is_valid():
            changepasswordForm.save()
            return redirect('Login:PAGE')
    else:
        changepasswordForm = PasswordChangeForm(user = require.user)

    Content = {'changepasswordForm':changepasswordForm, 'USER':require.user}
    return render(require, 'Login/change-password.html', Content)

# 上传文件
def upload(request,id):
    uf=userfile()
    if request.method == "POST":
        uf.username = request.user.username
        uf.homework = Homework.objects.get(id=id)
        uf.headImg = request.FILES.get('tttt',None)
        uf.save()
        messages.info(request,"上传成功")
        #return HttpResponse('upload ok!')
    return render(request,'Login/upload.html',{'uf':uf})

#增设课程（需要老师的权限）
def addcourse(request):
    Nowcourse = course()
    if request.method == "POST":
        Nowcourse.teacherName = request.user.username
        Nowcourse.courseNum = request.POST['courseNum']
        Nowcourse.courseName = request.POST['courseName']
        Nowcourse.save()
        messages.info(request,"添加成功")
        #return HttpResponse('添加成功')
    return render(request,'Login/addcourse.html',{'Nowcourse':Nowcourse})

#加入课程（需要学生的权限）
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

#展示课程细节
def coursedetail(request,id):
    mycourse=course.objects.get(id = id)
    sc = stucourse.objects.filter( thecourse_id = id)
    hw=Homework.objects.filter(courseNum = id)
    context = {'mycourse':mycourse,'sc':sc,'hw':hw}
    return render(request,'Login/coursedetail.html',context)

#删除课程
def coursedelete(request,id):
    target = course.objects.get(id=id)
    target.delete()
    messages.info(request,"已删除此课程")
    return redirect('Login:PAGE')

#为某门课添加助教（需要老师的权限）
def addassistant(request,id):
    assistant = asscourse()
    Course = course.objects.get(id=id)
    if request.method == "POST":
        assistant.assistantName = request.POST['assistantName']
        assistant.thecourse = Course
        assistant.save()
        messages.info(request,"添加成功")
        #return HttpResponse('添加成功')
    return render(request,'Login/addassistant.html',{'Course':Course})

#展示作业细节
def homeworkdetail(request,id):
    homework = Homework.objects.get(id=id)
    time = timezone.now()
    homework.Homework_text = markdown.markdown(homework.Homework_text,
        extensions=[
        # 包含 缩写、表格等常用扩展
        'markdown.extensions.extra',
        # 语法高亮扩展
        'markdown.extensions.codehilite',
        ])
    context = {'homework':homework,'time':time}
    return render(request,'Login/homeworkdetail.html',context)

#展示需要评论的列表
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

#某一个人的信息
def persondetail(request):
    user = request.GET['user']
    detail = User.objects.get(username = user )
    return render(request,'Login/persondetail.html',{'detail':detail})

#查看分数（需要学生的权限）
def checkcomments(request,id):
    homeworks = Homework.objects.filter(courseNum=id)
    comments = []
    for homework in homeworks:
        uploads = userfile.objects.filter(homework_id = homework.id)
        for upload in uploads:
            if upload.username == request.user.username:
                cm = Comment.objects.get(userfile_id = upload.id)
                comments.append(cm)
    context = {'comments':comments}
    return render(request,'Login/checkcomments.html',context)
                


