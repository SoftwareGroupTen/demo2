from django.urls import path
from . import views

app_name = 'comment'

urlpatterns = [
    path('postComment/', views.postComment, name='post_comment'),
    path('showComment/', views.showComment),
    path('deleteComment/', views.deleteComment),
]