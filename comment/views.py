from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import Comment
from .forms import CommentForm

# Create your views here.

def postComment(request):
    if request.method == 'POST':
        hwId=request.POST.get('hwId')
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            point=request.POST.get('point')
            body=request.POST.get('body')
            # commentModels.Comment.objects.create(homework_id=hwId, point=point, body=body)
            newComment=Comment()
            newComment.homework_id=hwId
            newComment.point=point
            newComment.body=body
            newComment.save()
        else:
            comment=Comment.objects.filter(homework=hwId)
            context = {'error': '输入内容有误或为空，请重新填写。', 'hwId': hwId, 'comment': comment}
            return render(request, 'comment/postComment.html', context)
    return render(request, 'comment/postComment.html')
'''
def deleteComment(request):
    commentId=request.GET.get('commentId')
    deleComment=Comment.objects.filter(id=int(commentId))
    deleComment.delete()
    hwId=request.GET.get('hwId')
    comment=Comment.objects.filter(homework=hwId)
    context = {'comment': comment}
    return render(request, 'comment:showComment.html', context)
    '''