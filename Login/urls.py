
from django.urls import path
from . import views

app_name = 'Login'
urlpatterns = [
    path('home/', views.PAGE, name = 'PAGE'),
    #path('login/', views.logIn, name = 'logIn'),
    path('logout/', views.logOut, name = 'logOut'),
    path('register/', views.Register, name = 'Register'),
    path('addcourse/', views.addcourse, name = 'addcourse'),
    path('joincourse/', views.joincourse, name = 'joincourse'),
    path('coursedetail/<int:id>',views.coursedetail, name = 'coursedetail'),
    path('homeworkdetail/<int:id>',views.homeworkdetail, name = 'homeworkdetail'),
    path('makecomments/', views.makecomments, name = 'makecomments'),
    path('coursedelete/<int:id>',views.coursedelete, name = 'coursedelete'),
    path('courserejust/<int:id>',views.courserejust, name = 'courserejust'),
    path('addassistant/<int:id>',views.addassistant, name = 'addassistant'),
    path('upload/<int:id>/',views.homeworkdetail,name = 'upload'),
    path('user-center/', views.usercenter, name = 'usercenter'),
    path('persondetail/',views.persondetail,name='persondetail'),
    path('user-center/edit-profile', views.editprofile, name = 'editprofile'),
    path('user-center/change-password', views.changepassword, name = 'changepassword'),
    path('checkcomments/<int:id>', views.checkcomments, name = 'checkcomments'),
]
