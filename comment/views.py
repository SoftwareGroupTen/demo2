from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from comment import models as commentModels
from upload import models as uploadModels
from .forms import CommentForm
from upload.models import userfile
from django.contrib.auth.models import User
from HomeworkPublish.models import Homework
from notifications.signals import notify
# Create your views here.

#通过get传参，针对某个上交的作业评分以及评论
def postComment(request):
    fileId=request.GET.get('fileId')
    hwId=request.GET.get('hwId')
    context = {'fileId': fileId, 'hwId': hwId}
    return render(request, 'comment/postComment.html', context)

#展示评论分数以及提交表单
def showComment(request):
    if request.method == 'POST':
        fileId=request.POST.get('fileId')
        hwId=request.POST.get('hwId')
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            point=request.POST.get('point')
            body=request.POST.get('body')
            newComment=commentModels.Comment()
            newComment.userfile_id=fileId
            newComment.point=point
            newComment.commentator=request.user.username
            newComment.body=body
            newComment.save()
            student = userfile.objects.get(homework_id=hwId)
            stu = User.objects.get(username = student.username )
            homework = Homework.objects.get(id=student.homework_id)
            notify.send(
                request.user,
                recipient=stu,
                verb='创建了新评论',
                target=homework,
                action_object=newComment,
                    
            ) 
        else:
            comment=commentModels.Comment.objects.filter(userfile=fileId)
            context = {'error': '输入内容有误或为空，请重新填写。', 'fileId': fileId, 'comment': comment, 'hwId': hwId}
            return render(request, 'comment/postComment.html', context)
    else:
        fileId=request.GET.get('fileId')
        hwId=request.GET.get('hwId')
    comment=commentModels.Comment.objects.filter(userfile=fileId)
    context = {'comment': comment, 'hwId': hwId}
    return render(request, 'comment/showComment.html', context)

#删除评论
def deleteComment(request):
    commentId=request.GET.get('commentId')
    deleComment=commentModels.Comment.objects.filter(id=int(commentId))
    deleComment.delete()
    fileId=request.GET.get('fileId')
    comment=commentModels.Comment.objects.filter(userfile=fileId)
    hwId=request.GET.get('hwId')
    context = {'comment': comment, 'hwId': hwId}
    return render(request, 'comment/showComment.html', context)