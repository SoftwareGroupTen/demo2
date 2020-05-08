from django.urls import path
from . import views

app_name = 'HomeworkPublish'

urlpatterns = [
    path('Homework_list/', views.Homework_list, name='Homework_list'),
    path('Homework_Publish/<int:id>',views.Homework_Publish,name='Homework_Publish'),
    path('Homework_delete/<int:id>/',views.Homework_delete,name='Homework_delete'),
]