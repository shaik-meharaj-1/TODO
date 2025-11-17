from django.urls import path 
from .views import *
urlpatterns = [
    path('',index,name='index'),
    path('post',post,name='post'),
    path('update/<int:id>/',update,name='update'),
    path('delete/<int:id>/',delete,name='delete'),
    path('complete/<int:id>/',complete,name='complete')
]
