from django.urls import path
from . import views

# 正在部署的应用的名称
app_name = "upload"

urlpatterns=[
    path('',views.register),
    path('filelist/',views.display,name="filelist"),
]